from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

CMD_QUIT: Command
CMD_RETR: Command
DESCRIPTOR: _descriptor.FileDescriptor
STAGE_FINI: Stage
STAGE_INIT: Stage
STAGE_RUN: Stage

class C2S(_message.Message):
    __slots__ = ["chunk", "file_name", "offset", "rs_size", "stage"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RS_SIZE_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    file_name: str
    offset: int
    rs_size: int
    stage: Stage
    def __init__(self, stage: _Optional[_Union[Stage, str]] = ..., file_name: _Optional[str] = ..., rs_size: _Optional[int] = ..., offset: _Optional[int] = ..., chunk: _Optional[bytes] = ...) -> None: ...

class S2C(_message.Message):
    __slots__ = ["cmd", "length", "offset", "result", "stage"]
    CMD_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    STAGE_FIELD_NUMBER: _ClassVar[int]
    cmd: Command
    length: int
    offset: int
    result: str
    stage: Stage
    def __init__(self, stage: _Optional[_Union[Stage, str]] = ..., cmd: _Optional[_Union[Command, str]] = ..., offset: _Optional[int] = ..., length: _Optional[int] = ..., result: _Optional[str] = ...) -> None: ...

class Stage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Command(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
