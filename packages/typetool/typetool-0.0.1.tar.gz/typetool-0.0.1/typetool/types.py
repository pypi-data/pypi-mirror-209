__all__ = [
        'JsonPrimitive',
        'DetaData',
        'DetaKey',
        'ExpireAt',
        'ExpireIn',
        'Jsonable',
        'JsonSequence',
        'DetaQuery',
        'ExistParams',
        'SearchParam',
        'ParserEntry',
        'ParserResult',
        'GenericType',
        'Number',
        'ParserReturn',
        'Types',
        'TypeArgs',
        'TupleMapTypes',
        'TupleSequenceTypes',
        'Undefined'
]

import datetime
from collections import ChainMap, deque, UserDict, UserList
from typing import Union, TypeVar
from decimal import Decimal


Undefined = object()

JsonPrimitive = Union[str, float, int, bool, None]
DetaData = Union[dict, list, str, float, int, bool]
DetaKey = Union[str, None]
ExpireIn = Union[str, None]
ExpireAt = Union[datetime.datetime, int, float, None]
JsonSequence = list[JsonPrimitive]
JsonDict = dict[str, Union[JsonSequence, JsonPrimitive]]
Jsonable = Union[JsonDict, JsonSequence, JsonPrimitive]
DetaQuery = Union[dict[str, JsonPrimitive], list[dict[str, JsonPrimitive]]]
ExistParams = Union[list[str], str]
SearchParam = str
ParserEntry = TypeVar('ParserEntry')
ParserResult = TypeVar('ParserResult')
ParserReturn = Union[ParserEntry, ParserResult]
GenericType = TypeVar('GenericType')
Number = TypeVar('Number', float, int, Decimal)
TypeArgs = tuple[type]
Types = Union[type, TypeArgs]
TupleSequenceTypes = (tuple, list, set, deque, UserList)
TupleMapTypes = (dict, UserDict, ChainMap)

