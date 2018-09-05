# -*- coding: utf-8 -*-
import json
from enum import Enum
from typing import List

__all__ = ['ExportProfile', 'TimeFormat']


class TimeFormat(Enum):
    ISO8601 = '%Y-%m-%dT%H:%M:%S.%f%z'


class ExportProfile:
    __profiles = {}

    @classmethod
    def register(cls, profile):
        cls.__profiles[profile.name] = profile

    @classmethod
    def profiles(cls):
        yield from cls.__profiles.values()

    @classmethod
    def names(cls):
        yield from cls.__profiles.keys()

    def copy(self) -> 'ExportProfile':
        return ExportProfile(**self.__dict__)

    def __init__(self, name: str, columns: List[str] = None, ext: str = 'dat',
                 precision: int = 10, dateformat: TimeFormat = TimeFormat.ISO8601,
                 _userprofile: bool = True, register: bool = True):
        self.name = name
        self.columns = columns or []
        self.ext = ext
        self.precision = precision

        if isinstance(dateformat, str):
            self.dateformat = TimeFormat(dateformat)
        else:
            self.dateformat = dateformat
        self._userprofile = _userprofile

        if register:
            ExportProfile.register(self)

    @property
    def readonly(self) -> bool:
        return not self._userprofile

    def to_json(self, indent=None) -> str:
        def _encode(val):
            if isinstance(val, TimeFormat):
                return val.value

        return json.dumps(self.__dict__, indent=indent, default=_encode)

    @classmethod
    def from_json(cls, value: str) -> 'ExportProfile':
        def _decode(obj):
            return cls(**obj)
        return json.loads(value, object_hook=_decode)