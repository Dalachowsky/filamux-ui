from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SetSpoolParamsReq(_message.Message):
    __slots__ = ["index", "length"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    index: int
    length: int
    def __init__(self, index: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class SetSpoolParamsRes(_message.Message):
    __slots__ = ["ok", "reason"]
    OK_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    reason: str
    def __init__(self, ok: bool = ..., reason: _Optional[str] = ...) -> None: ...
