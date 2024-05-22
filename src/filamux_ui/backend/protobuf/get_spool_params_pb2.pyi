from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetSpoolParamsReq(_message.Message):
    __slots__ = ["index"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    index: int
    def __init__(self, index: _Optional[int] = ...) -> None: ...

class GetSpoolParamsRes(_message.Message):
    __slots__ = ["active", "lengthRemaining"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LENGTHREMAINING_FIELD_NUMBER: _ClassVar[int]
    active: bool
    lengthRemaining: int
    def __init__(self, active: bool = ..., lengthRemaining: _Optional[int] = ...) -> None: ...
