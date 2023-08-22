from _typeshed import Incomplete, Unused
from typing import NoReturn
from typing_extensions import Self

from ._imaging import _PixelAccessor
from .Image import Image

MAXBLOCK: int
SAFEBLOCK: Incomplete
LOAD_TRUNCATED_IMAGES: bool
ERRORS: Incomplete

def raise_oserror(error) -> NoReturn: ...

class ImageFile(Image):
    custom_mimetype: Incomplete
    tile: list[Incomplete] | None
    readonly: int
    decoderconfig: Incomplete
    decodermaxblock: Incomplete
    fp: Incomplete
    filename: Incomplete
    def __init__(self, fp: Incomplete | None = None, filename: Incomplete | None = None) -> None: ...
    def get_format_mimetype(self): ...
    def verify(self) -> None: ...
    map: Incomplete
    im: Incomplete
    def load(self) -> _PixelAccessor: ...
    def load_prepare(self) -> None: ...
    def load_end(self) -> None: ...

class StubImageFile(ImageFile):
    def load(self) -> _PixelAccessor: ...

class Parser:
    incremental: Incomplete | None
    image: Incomplete | None
    data: Incomplete | None
    decoder: Incomplete | None
    offset: int
    finished: bool
    def reset(self) -> None: ...
    decode: Incomplete
    def feed(self, data) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...
    def close(self) -> Image: ...

class PyCodecState:
    xsize: int
    ysize: int
    xoff: int
    yoff: int
    def extents(self) -> tuple[int, int, int, int]: ...

class PyCodec:
    im: Incomplete
    state: Incomplete
    fd: Incomplete
    mode: Incomplete
    def __init__(self, mode, *args) -> None: ...
    args: Incomplete
    def init(self, args) -> None: ...
    def cleanup(self) -> None: ...
    def setfd(self, fd) -> None: ...
    def setimage(self, im, extents: Incomplete | None = None) -> None: ...

class PyDecoder:
    im: Incomplete
    state: Incomplete
    fd: Incomplete
    mode: Incomplete
    def __init__(self, mode, *args) -> None: ...
    args: Incomplete
    def init(self, args) -> None: ...
    @property
    def pulls_fd(self): ...
    def decode(self, buffer) -> tuple[int, int]: ...
    def cleanup(self) -> None: ...
    def setfd(self, fd) -> None: ...
    def setimage(self, im, extents: Incomplete | None = None) -> None: ...
    def set_as_raw(self, data, rawmode: Incomplete | None = None) -> None: ...

class PyEncoder(PyCodec):
    @property
    def pushes_fd(self): ...
    def encode(self, bufsize) -> None: ...
    def encode_to_pyfd(self): ...
    def encode_to_file(self, fh, bufsize): ...
