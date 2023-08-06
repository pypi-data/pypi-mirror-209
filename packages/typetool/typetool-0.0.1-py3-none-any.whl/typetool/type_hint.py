__all__ = [
        'isinstance_of_type',
        'is_dataclass_instance',
        'is_dataclass_type',
        'TypeHint',
        'no_value',
        'is_missing',
        'is_none',
        'is_empty_string',
        'is_undefined',
]

import re
import datetime
from abc import ABC
from collections import ChainMap, deque
from typing import Union
from decimal import Decimal
from dataclasses import is_dataclass, MISSING
from typing import Any, get_args, get_origin
from .base_models import *
from .types import *
from .protocols import *



class Parser(ABC):
    @classmethod
    def get(cls, value: ParserEntry, cast_type: type[ParserResult]):
        return cls.process(value, cast_type)

    @classmethod
    def process(cls, value: ParserEntry, cast_type: type[ParserResult]) -> ParserReturn:
        cast_analysis = TypeHint(cast_type)
        if cast_analysis.check_type(value):
            return value
        try:
            if cast_analysis.is_simple_type:
                if isinstance(value, cast_type):
                    return value
                elif no_value(value):
                    return ''
                return cls.simple_engine(cast_type)(value)
            elif cast_analysis.is_sequence:
                return cls.sequence_engine(value, cast_analysis.origin, cast_analysis.args)
            elif cast_analysis.is_mapping:
                return cls.mapping_engine(value, cast_analysis.origin, cast_analysis.args)
            else:
                return cls.generic_engine(value, cast_type)
        except ValueError as e:
            print(e)
            return value

    @classmethod
    def simple_engine(cls, cast_type: type[ParserResult]) -> ParserProtocol:
        if cast_type is str:
            return cls.str_engine
        elif cast_type is int:
            return cls.int_engine
        elif cast_type is float:
            return cls.float_engine
        elif cast_type is datetime.date:
            return cls.date_engine
        elif cast_type is datetime.datetime:
            return cls.datetime_engine
        elif cast_type is bytes:
            return cls.bytes_engine
        elif cast_type is Decimal:
            return cls.decimal_engine
        elif cast_type is list:
            return cls.list_engine
        elif cast_type is set:
            return cls.set_engine
        elif cast_type is tuple:
            return cls.tuple_engine
        elif issubclass(cast_type, BaseDetaModel):
            return cls.str_engine
        elif issubclass(cast_type, EnumModel):
            return lambda value: cls.enum_engine(value, cast_type)
        elif issubclass(cast_type, (DictModel, StringListModel, Regex)):
            return cast_type

    @classmethod
    def sequence_engine(cls, value: ParserEntry, origin: type, args: tuple[type]) -> ParserReturn:
        if origin is list:
            if isinstance(value, (list, tuple, set)):
                return [cls.get(item, args[0]) for item in value]
            else:
                return [cls.get(value, args[0])]
        elif origin in [set, tuple]:
            if isinstance(value, (list, tuple, set)):
                return origin([cls.get(item, args[0]) for item in value])
            else:
                return origin([cls.get(value, args[0])])

    @classmethod
    def mapping_engine(cls, value: ParserEntry, origin: Union[dict, ChainMap], args: tuple[type]) -> ParserReturn:
        if origin is dict:
            if isinstance(value, (ChainMap, dict)):
                return {cls.get(k, args[0]): cls.get(v, args[-1]) for k, v in value.items()}
        elif origin is ChainMap:
            if isinstance(value, (ChainMap, dict)):
                return ChainMap({cls.get(k, args[0]): cls.get(v, args[-1]) for k, v in value.items()})

    @classmethod
    def generic_engine(cls, value: ParserEntry, generic: ParserResult) -> ParserReturn:
        if generic is Number:
            return cls.number_engine(value)

    @classmethod
    def list_engine(cls, value: ParserEntry) -> ParserReturn:
        if isinstance(value, (set, tuple)):
            return [*value]
        return value if isinstance(value, list) else [value]

    @classmethod
    def set_engine(cls, value: ParserEntry) -> ParserReturn:
        if isinstance(value, (list, tuple)):
            return {**value}
        return value if isinstance(value, set) else {value}

    @classmethod
    def tuple_engine(cls, value: ParserEntry) -> ParserReturn:
        if isinstance(value, (list, set)):
            return tuple([*value])
        return value if isinstance(value, tuple) else tuple([value])

    @classmethod
    def str_engine(cls, value: ParserEntry) -> ParserReturn:
        return str(value)

    @classmethod
    def int_engine(cls, value):
        if isinstance(value, str):
            return int(float(re.sub(r',', '.', value)).__round__(0))
        elif isinstance(value, Decimal):
            return int(value)
        elif isinstance(value, (datetime.date, datetime.datetime)):
            return value.toordinal()
        return value

    @classmethod
    def float_engine(cls, value):
        if isinstance(value, str):
            return float(re.sub(r',', '.', value))
        elif isinstance(value, int):
            return float(value)
        elif isinstance(value, Decimal):
            return float(value)
        elif isinstance(value, bytes):
            return float(re.sub(r',', '.', value.decode('utf-8')))
        return value

    @classmethod
    def date_engine(cls, value: ParserEntry) -> ParserReturn:
        if isinstance(value, str):
            return datetime.date.fromisoformat(value)
        elif isinstance(value, datetime.datetime):
            return value.date()
        elif isinstance(value, int):
            return datetime.date.fromordinal(value)

    @classmethod
    def enum_engine(cls, value: ParserEntry, enum_type: type[EnumModel]) -> ParserReturn:
        try:
            return enum_type[value]
        except BaseException as e:
            print(e)
            return enum_type(value)

    @classmethod
    def datetime_engine(cls, value: ParserEntry) -> ParserReturn:
        if isinstance(value, str):
            return datetime.datetime.fromisoformat(value)
        elif isinstance(value, datetime.date):
            return datetime.datetime.fromordinal(value.toordinal())
        elif isinstance(value, int):
            return datetime.datetime.fromordinal(value)

    @classmethod
    def bytes_engine(cls, value: ParserEntry) -> ParserReturn:
        return str(value).encode('utf-8')

    @classmethod
    def decimal_engine(cls, value: ParserEntry) -> ParserReturn:
        if isinstance(value, str):
            return Decimal(re.sub(r',', '.', value))

    @classmethod
    def number_engine(cls, value: ParserEntry) -> ParserReturn:
        if isinstance(value, str):
            if re.match(r'\.,', value):
                return cls.get(value, float)
            else:
                return cls.get(value, int)
        elif isinstance(value, (datetime.date, datetime.datetime)):
            return value.toordinal()



def is_undefined(value: Any) -> bool:
    return value is Undefined


def is_none(value: Any) -> bool:
    return value is None


def is_missing(value: Any) -> bool:
    return value is MISSING


def is_empty_string(value: Any) -> bool:
    return value == ''


def no_value(value: Any) -> bool:
    return is_none(value) or is_undefined(value) or is_empty_string(value) or is_missing(value) or is_empty_sequence(
            value) or is_empty_map(value)


def is_empty_sequence(value: Any) -> bool:
    return True if isinstance(value, TupleSequenceTypes) and len(value) == 0 else False


def is_empty_map(value: Any) -> bool:
    return True if isinstance(value, TupleMapTypes) and len(value) == 0 else False


def isinstance_of_type(obj: Any) -> bool:
    return isinstance(obj, type)


def is_dataclass_type(obj: Any) -> bool:
    return not is_dataclass_instance(obj) and is_dataclass(obj)


def is_dataclass_instance(obj: Any) -> bool:
    return is_dataclass(obj) and not isinstance_of_type(obj)


class TypeHint:
    def __init__(self, type_hint):
        self.type_hint = type_hint
        
    def __str__(self):
        return f'{type(self).__name__}({self.type_hint})'
    
    @property
    def args(self) -> tuple[type]:
        return tuple([t for t in get_args(self.type_hint) if isinstance(t, type) if t is not type(None)])
    
    @property
    def is_args_generic(self):
        return all([not isinstance_of_type(item) for item in self.args])
    
    @property
    def origin(self):
        return get_origin(self.type_hint)
    
    @property
    def is_sequence(self):
        return self.origin in TupleSequenceTypes
    
    @property
    def is_mapping(self):
        return self.origin in TupleMapTypes
    
    @property
    def is_generic(self):
        return not isinstance_of_type(self.origin)
    
    @property
    def is_simple_type(self) -> bool:
        return not self.args and isinstance_of_type(self.type_hint)
    
    @property
    def is_optional(self):
        return type(None) in self.args
    
    @property
    def expected_type(self):
        if self.is_simple_type:
            return self.type_hint
        elif self.is_mapping or self.is_sequence:
            return self.origin
        else:
            return self.args
    
    @property
    def is_dict_model(self):
        return issubclass(self.type_hint, DictModel)
    
    @property
    def is_deta_model(self):
        return issubclass(self.type_hint, BaseDetaModel)
    
    @property
    def is_string_list_model(self):
        return issubclass(self.type_hint, StringListModel)
    
    def check_type(self, value: Any) -> bool:
        if self.is_simple_type:
            if self.is_deta_model:
                return isinstance(value, str)
            elif self.is_dict_model:
                return isinstance(value, dict)
            elif self.is_string_list_model:
                return isinstance(value, list) and all([isinstance(item, str) for item in value])
            return isinstance(value, self.type_hint)
        elif self.is_generic:
            return isinstance(value, self.args)
        elif self.is_sequence:
            return isinstance(value, self.origin) and all([isinstance(item, self.args) for item in value])
        elif self.is_mapping:
            return isinstance(value, self.origin) and all(
                    [isinstance(item, tuple(self.args[1:])) for item in value.values()]) and all(
                    [isinstance(item, self.args[0]) for item in value.keys()])
        else:
            return False
        
        

    def parse(self, value: ParserEntry) -> ParserResult:
        if self.check_type(value):
            return value
        return Parser.get(value, self.type_hint)
            

