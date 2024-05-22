from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetStatusReq(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetStatusRes(_message.Message):
    __slots__ = ["currentSpool", "status", "statusExchange"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class StatusExchange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CHANGING: GetStatusRes.StatusExchange
    CURRENTSPOOL_FIELD_NUMBER: _ClassVar[int]
    ERROR: GetStatusRes.Status
    ERROR_FILAMENT_RUNOUT: GetStatusRes.Status
    FEEDING: GetStatusRes.StatusExchange
    FILAMENT_EXCHANGE: GetStatusRes.Status
    OK: GetStatusRes.Status
    RETRACTING: GetStatusRes.StatusExchange
    STATUSEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    currentSpool: int
    status: GetStatusRes.Status
    statusExchange: GetStatusRes.StatusExchange
    def __init__(self, status: _Optional[_Union[GetStatusRes.Status, str]] = ..., statusExchange: _Optional[_Union[GetStatusRes.StatusExchange, str]] = ..., currentSpool: _Optional[int] = ...) -> None: ...
