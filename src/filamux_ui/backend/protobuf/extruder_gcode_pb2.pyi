from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExtruderGCodeReq(_message.Message):
    __slots__ = ["gcode"]
    GCODE_FIELD_NUMBER: _ClassVar[int]
    gcode: str
    def __init__(self, gcode: _Optional[str] = ...) -> None: ...

class ExtruderGCodeRes(_message.Message):
    __slots__ = ["status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ERROR: ExtruderGCodeRes.Status
    OK: ExtruderGCodeRes.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: ExtruderGCodeRes.Status
    def __init__(self, status: _Optional[_Union[ExtruderGCodeRes.Status, str]] = ...) -> None: ...
