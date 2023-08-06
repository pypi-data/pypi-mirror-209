import os
from pathlib import Path
from typing import List, Tuple, Dict, Any
import depthai as dai

try:
    import cv2
except ImportError:
    cv2 = None

from depthai_sdk.readers.abstract_reader import AbstractReader
from depthai_sdk.components.parser import parse_camera_socket

_videoExt = ['.mjpeg', '.avi', '.mp4', '.h265', '.h264']


class VideoCapReader(AbstractReader):
    """
    Reads stream from mp4, mjpeg, h264, h265
    """

    def __init__(self, path: Path, loop: bool = False) -> None:
        self.initialFrames: Dict[str, Any] = dict()
        self.shapes: Dict[str, Tuple[int, int]] = dict()
        self.readers: Dict[str, cv2.VideoCapture] = dict()
        self._is_looped = loop

        if path.is_file():
            stream = path.stem if (path.stem in ['left', 'right']) else 'color'
            self.readers[stream] = cv2.VideoCapture(str(path))
        else:
            for fileName in os.listdir(str(path)):
                f_name, ext = os.path.splitext(fileName)
                if ext not in _videoExt:
                    continue

                # Check if name of the file starts with left.. right.., or CameraBoardSocket
                if f_name.startswith('CameraBoardSocket'):
                    f_name = f_name.split('CameraBoardSocket.')[1]

                try:
                    socket = parse_camera_socket(f_name)
                except ValueError:
                    # Invalid file name
                    continue

                # TODO: avoid changing stream names, just use socket
                stream = str(socket)
                if socket == dai.CameraBoardSocket.CAM_A:
                    stream = 'color'
                elif socket == dai.CameraBoardSocket.CAM_B:
                    stream = 'left'
                elif socket == dai.CameraBoardSocket.CAM_C:
                    stream = 'right'

                self.readers[stream] = cv2.VideoCapture(str(path / fileName))

        for name, reader in self.readers.items():
            ok, f = reader.read()
            self.shapes[name] = (
                f.shape[1],
                f.shape[0]
            )
            self.initialFrames[name] = f

    def read(self):
        frames = dict()
        for name, reader in self.readers.items():
            if self.initialFrames[name] is not None:
                frames[name] = self.initialFrames[name].copy()
                self.initialFrames[name] = None

            if not self.readers[name].isOpened():
                return False

            ok, frame = self.readers[name].read()
            if not ok and self._is_looped:
                self.readers[name].set(cv2.CAP_PROP_POS_FRAMES, 0)
                ok, frame = self.readers[name].read()
            elif not ok:
                return False

            frames[name] = frame

        return frames

    def set_loop(self, loop: bool):
        self._is_looped = loop

    def getStreams(self) -> List[str]:
        return [name for name in self.readers]

    def getShape(self, name: str) -> Tuple[int, int]:  # Doesn't work as expected!!
        return self.shapes[name]

    def close(self):
        [r.release() for _, r in self.readers.items()]

    def disableStream(self, name: str):
        if name in self.readers:
            self.readers.pop(name)

    def get_message_size(self, name: str) -> int:
        return self.shapes[name][0] * self.shapes[name][1] * 3
