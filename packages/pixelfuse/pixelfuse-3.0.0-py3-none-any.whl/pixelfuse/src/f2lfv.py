import hashlib
import os
from pathlib import Path
import pickle
import struct

import cv2
import numpy as np
from rich import print
from rich.progress import (BarColumn, MofNCompleteColumn, Progress,
                           SpinnerColumn, TimeElapsedColumn,
                           TimeRemainingColumn)

from pixelfuse import lessf_encoder


class ToLessFragileVideo(object):
    def __init__(self, file: Path, fps=1., width=640, height=480, fourcc="HFYU", output: Path=Path("output.avi"), verbose=2, hashmap=None):
        self.file = file
        self.fps = fps
        self.width = width
        self.height = height
        self.fourcc = cv2.VideoWriter_fourcc(*fourcc)
        self.output = output
        self.checksum = hashlib.sha512(self.file.read_bytes()).hexdigest()
        self.verbose = verbose
        self.hashmap = hashmap

        self.bytesInFile = self.file.stat().st_size
        self.pixelsInFile = self.bytesInFile

        self.barColumns = [
            SpinnerColumn(),
            "{task.description}",
            BarColumn(),
            "Elapsed time:",
            TimeElapsedColumn(),
            "Remaining time:",
            TimeRemainingColumn(),
            "Completed pixels:",
            MofNCompleteColumn()
        ]
        self.barKwargs = {
            "transient": True
        }

    def convert(self):
        out = cv2.VideoWriter(self.output.name, self.fourcc, self.fps, (self.width, self.height))

        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.print("Opening the file...", 1)
        with self.file.open("rb") as f:
            y = 0
            x = 0
            self.print("Creating meta data...", 2)
            meta = {
                "checksum": self.checksum,
                "filename": self.file.name,
                "encoder": lessf_encoder,
                "hashmap": self.hashmap,
                "end": None
            }

            self.print("Starting video writing...", 1)
            with Progress(*self.barColumns, **self.barKwargs) as progress:
                for i in progress.track(range(self.pixelsInFile)):
                    b = f.read(1)
                    if not b:
                        self.print("File end", 3)
                        break

                    bits = self.bits(b)

                    for bit in bits:
                        frame[y, x] = (bit*255, bit*255, bit*255)
                        x += 1
                        if x >= self.width:
                            x = 0
                            y += 1
                        if y >= self.height:
                            self.print(f"Done {frame[0, 0:24, 0]} frame", 2)
                            out.write(frame)
                            y = 0
                            frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)

                if np.any(frame):
                    self.print(f"Writing not full {frame[0, 0:24, 0]} frame", 2)
                    print(x, y)
                    meta["end"] = x*y
                    out.write(frame)

                self.print(f"Creating meta data frame...", 3)
                pickle_bytes = pickle.dumps(meta)
                frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
                x = 0
                y = 0

                for bit in self.pickleToBits(pickle_bytes):
                    frame[y, x] = [bit*255, bit*255, bit*255]
                    x += 1
                    if x >= self.width:
                        x = 0
                        y += 1

                self.print(f"Writing meta data {frame[0, 0:3, 0]} frame", 2)
                out.write(frame)

                # frame[frame > 127] = 1
                # frame = list(self.pickleToBits(pickle_bytes))

                # byte_array = bytearray()
                # for i in range(0, len(frame), 8):
                #     byte = 0
                #     for j in range(8):
                #         if i + j < len(frame):
                #             byte |= frame[i + j] << j
                #     byte_array.append(byte)

                # print(pickle.loads(byte_array))

        self.print(f"Writing video...", 1)
        out.release()

    def print(self, text, verbose):
        if self.verbose >= verbose:
            print(text)

    def bits(self, b):
        b = ord(b)
        for _ in reversed(range(8)):
            yield b & 1
            b >>= 1

    def pickleToBits(self, pickleString):
        bit_list = []
        for byte in pickleString:
            for i in range(8):
                bit = (byte >> i) & 1
                bit_list.append(bit)

        return bit_list
    