from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
MSG_EXTRUDER_FEED: MessageType
MSG_EXTRUDER_GCODE: MessageType
MSG_GET_SPOOL_PARAMS: MessageType
MSG_GET_STATUS: MessageType
MSG_SET_SPOOL_PARAMS: MessageType
MSG_SET_TARGET_SPOOL: MessageType

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
