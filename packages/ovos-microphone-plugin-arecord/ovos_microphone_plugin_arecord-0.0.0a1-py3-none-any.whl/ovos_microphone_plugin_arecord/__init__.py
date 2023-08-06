# Copyright 2022 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import subprocess
from dataclasses import dataclass
from threading import Thread, Lock
from typing import Optional

from ovos_plugin_manager.templates.microphone import Microphone



class RingBuffer:

    def __init__(self, buffer_size=32768):
        self.read_pos = 0
        self.write_pos = self.write_pos_old = 0
        self.buffer_size = buffer_size
        self.buffer = bytearray(self.buffer_size)
        self.lock = Lock()

    def write(self, data):

        if not data:
            return

        datalen = len(data)

        if datalen > self.buffer_size:
            print("Trying to write huge buffer !!!!!!!")
            return

        self.lock.acquire()

        # TODO: Check for buffer overrun
        # Case A: Read pos was smaller than write pos
        # Case B: Read pos was bigger than write pos
        self.write_pos_old = self.write_pos
        # Data fitting into remaining buffer
        if self.write_pos + datalen <= self.buffer_size:
            self.buffer[self.write_pos:self.write_pos + datalen] = data[:]
            self.write_pos += datalen

        else:

            # Write first part into buffer
            first_len = self.buffer_size - self.write_pos
            self.buffer[self.write_pos:self.write_pos + first_len] = data[
                                                                     0:first_len]

            # Write second part wrapped around
            second_len = datalen - first_len
            self.buffer[0:second_len] = data[first_len:first_len + datalen]
            self.write_pos = second_len

        self.lock.release()

    def get_buffer_size(self):
        return self.buffer_size

    def can_read_n_bytes(self, n):
        if self.read_pos <= self.write_pos:
            return n <= self.write_pos - self.read_pos
        else:
            avail = self.buffer_size - self.read_pos + self.write_pos
            return n <= avail

    def read(self, blocksize, advance):

        self.lock.acquire()

        # Not enough data for reading
        if not self.can_read_n_bytes(blocksize):
            self.lock.release()
            return None

        # Can read in one block
        if self.read_pos + blocksize <= self.buffer_size:
            data = self.buffer[self.read_pos:self.read_pos + blocksize]
            self.read_pos += advance
            if self.read_pos > self.buffer_size:
                self.read_pos %= self.buffer_size

            self.lock.release()
            return data

        # Need to concatenate
        else:

            first_part = self.buffer[self.read_pos:self.buffer_size]
            first_len = self.buffer_size - self.read_pos
            second_len = blocksize - first_len
            second_part = self.buffer[0:second_len]
            self.read_pos += advance
            if self.read_pos > self.buffer_size:
                self.read_pos %= self.buffer_size

            data = first_part + second_part

            self.lock.release()
            return data


class ArecordStream(Thread):
    # Efficiently capture audio into a ringbuffer using arecord
    # This will only work for linux based systems

    # To minimize CPU usage large chunks are read from alsa
    # The audio capture is running in its own thread
    # Reading from the buffer is blocking
    def __init__(self, sample_rate=16000, channels=1, audio_length=80):
        Thread.__init__(self, daemon=True)

        self.running = False
        self.input_device = 'default'
        self.bytes_per_sample = 2
        self.sample_rate = sample_rate
        self.channels = channels
        self.audio_length = audio_length
        self.blocksize = int((self.sample_rate * (
            self.audio_length) / 1000) * self.channels * self.bytes_per_sample)

        self._cmd = [
            'arecord',
            '-q',
            '-t', 'raw',
            '-D', self.input_device,
            '-c', str(self.channels),
            '-f', 's16',
            '-r', str(self.sample_rate),
        ]

        self._arecord = None
        self.audio_buffer = RingBuffer()

    def print_info(self):
        print("Blocksize: " + str(self.blocksize))
        print("Sample Rate: " + str(self.sample_rate))
        print("Channels: " + str(self.channels))

    # Get len number of samples
    # Blocks until samples is available
    def read(self, chunk_size=None, advance=None):
        chunk_size = chunk_size or self.blocksize
        advance = advance or chunk_size
        return self.audio_buffer.read(chunk_size, advance)

    def stop(self):
        self.running = False

    def run(self):
        self._arecord = subprocess.Popen(self._cmd, stdout=subprocess.PIPE)
        self.running = True
        while self._arecord and self.running:
            input_data = self._arecord.stdout.read(self.blocksize)
            if input_data:
                self.audio_buffer.write(input_data)

        # Shutdown record command
        if self._arecord:
            self._arecord.kill()
            self._arecord = None


@dataclass
class ArecordMicrophone(Microphone):
    arecord: ArecordStream = None

    def start(self):
        self.arecord = ArecordStream(sample_rate=self.sample_rate,
                                     channels=self.sample_channels)
        self.arecord.start()

    def read_chunk(self) -> Optional[bytes]:
        return self.arecord.read(chunk_size=self.chunk_size)

    def stop(self):
        self.arecord.stop()
