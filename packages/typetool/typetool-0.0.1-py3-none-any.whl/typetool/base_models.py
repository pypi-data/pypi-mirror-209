__all__ = [ 'DictModel', 'BaseDetaModel', 'BaseModel', 'StringModel', 'EnumModel', 'Regex', 'ListModel',
            'StringListModel']

import re
from inspect import signature
from enum import Enum
from abc import ABC, abstractmethod
from typing import Collection, Any, Iterable, ClassVar, Optional, get_type_hints
from dataclasses import dataclass, field
from collections import UserDict, UserList, UserString, deque, ChainMap
from .types import *
from .functions import *



class EnumModel(Enum):
    
    @classmethod
    def table(cls):
        return cls.__name__
    
    def json(self):
        return self.name
    
    @property
    def key(self):
        return self.name
    
    def __str__(self):
        return self.value
    
    @property
    def display(self):
        return self.value
    
    @classmethod
    def members(cls):
        return cls.__members__.values()
    
    @classmethod
    def option(cls, item: 'EnumModel' = None, selected: bool = False):
        if not item:
            return '<option></option>'
        return f'<option id="{type(item).__name__}.{item.key}" value="{item.key}" ' \
               f'{"selected" if selected is True else ""}>{item.display}</option>'
    
    @classmethod
    def options(cls, default: str = None):
        if default:
            if isinstance(default, cls):
                default = default.name
        return ''.join([cls.option(member, member.key == default) for member in cls.members()])
    



@dataclass
class DataClassModel(ABC):
    @classmethod
    def class_name(cls):
        return cls.__name__
    
    @classmethod
    def type_hints(cls):
        return get_type_hints(cls)


@dataclass
class BaseDetaModel(DataClassModel):
    TABLE: ClassVar[Optional[str]] = None
    ITEM_NAME: ClassVar[Optional[str]] = None
    DETA_QUERY: ClassVar[Optional[DetaQuery]] = None
    
    @property
    def get_key(self):
        return getattr(self, 'key', None)
    
    @classmethod
    def table(cls):
        return cls.TABLE or cls.class_name()
    
    @classmethod
    def item_name(cls):
        """ITEM_NAME or slug of table name"""
        return cls.ITEM_NAME or slug(cls.table())
    
    @classmethod
    @abstractmethod
    async def fetch_all(cls, query: DetaQuery = None) -> list[dict]:
        return NotImplemented
    
    
@dataclass
class BaseModel(DataClassModel):
    pass


class DictModel(UserDict):
    def __init__(self, *args, **kwargs):
        self.args = [*args]
        self.kwargs = kwargs
        super().__init__(self.setup())
        
    def setup(self) -> dict:
        data = self.kwargs
        for item in reversed(self.args):
            if isinstance(item, dict):
                data.update(self.args)
        return data
        
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return '{}({})'.format(
                type(self).__name__,
                ', '.join([f'{k}={v}' if not isinstance(v, str) else f'{k}="{v}"' for k, v in self.data.items() if v])
        )
    def append(self, value: Any):
        self.args.append(value)
        
    def include(self, **kwargs):
        self.data.update(kwargs)
    
    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, item):
        return self.data.get(item, None)

    def __delitem__(self, key):
        try:
            del self.data[key]
        finally:
            pass

    
class StringModel(UserString):
    def __init__(self, *args, **kwargs):
        self.args = [*args]
        self.kwargs = kwargs
        super().__init__(self.setup())
    
    def setup(self) -> str:
        if len(self.args) > 0:
            data = str(self.args.pop(0))
        else:
            data = str()
        return data
        
        
class ListModel(UserList):
    def __init__(self, *args, **kwargs):
        self.args = [*args]
        self.kwargs = kwargs
        super().__init__(self.setup())
    
    def setup(self) -> list:
        data = list()
        for item in self.args:
            if isinstance(item, (list, set, deque)):
                data.extend([*item])
            else:
                data.append(item)
        return data
    
    def include(self, *args):
        for item in args:
            if isinstance(item, (list, set, deque)):
                self.data.extend(item)
            else:
                self.data.append(item)
    

class StringListModel(ListModel):
    
    def setup(self) -> list:
        return [str(i) for i in super().setup()]
    
    def include(self, *args):
        for item in args:
            if isinstance(item, (set, list, deque)):
                self.extend(item)
            else:
                self.append(item)
    
    def append(self, item: str) -> None:
        if item:
            self.data.append(str(item))
        pass
    
    def extend(self, items: Collection[Any]) -> None:
        self.data.extend([str(i) for i in items if i])
        

class Regex(UserString):
    def __init__(self, value: str = ""):
        self.string = value
        super().__init__(self.render())
    
    def __repr__(self):
        return f'{type(self).__name__}({self.data})'
    
    @classmethod
    def normalize_whitespaces(cls, value: str):
        return ' '.join([i for i in re.split(r'\s+', value) if i]).strip()
    
    @classmethod
    def normalize_final_point(cls, value: str):
        return re.sub(r'\s+\.|\s\.', '.', value)
    
    @classmethod
    def special_join(cls, seq: Iterable[Any], sep: str = " ") -> str:
        return sep.join([str(item) for item in seq if item])
    
    @classmethod
    def split_lines(cls, value: str):
        return [i for i in [cls.normalize_whitespaces(i) for i in re.split(r'\n\r|\n', value)] if i]
    
    @property
    def digits(self):
        return ''.join(re.findall(r'\d', self.string))
    
    @property
    def words(self):
        return re.split(r'\s+|\s', self.string)
    
    def render(self):
        return self.string
    
    def export(self):
        return self.data
    
    def asjson(self):
        return self.export()

