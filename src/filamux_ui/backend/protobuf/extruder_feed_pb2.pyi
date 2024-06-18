from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExtruderFeedReq(_message.Message):
    __slots__ = ["distance", "speed"]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    distance: int
    speed: int
    def __init__(self, speed: _Optional[int] = ..., distance: _Optional[int] = ...) -> None: ...

class ExtruderFeedRes(_message.Message):
    __slots__ = ["ok", "reason"]
    OK_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    reason: str
    def __init__(self, ok: bool = ..., reason: _Optional[str] = ...) -> None: ...
