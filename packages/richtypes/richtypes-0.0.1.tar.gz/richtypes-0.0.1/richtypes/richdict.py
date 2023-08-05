from copy import deepcopy
from typing import Callable, TypeVar

T = TypeVar("T")


class RichDict(dict):
    def __init__(self, **args: object) -> None:
        super().__init__(args)

    @property
    def length(self):
        return len(self)

    @property
    def is_empty(self):
        return len(self) == 0

    @property
    def is_not_empty(self):
        return len(self) > 0

    @property
    def first_item(self):
        if self:
            for key in self:
                return {key: self[key]}
        else:
            raise IndexError("Dict index out of range")

    @property
    def first_key(self):
        if self:
            for key in self:
                return key
        else:
            raise IndexError("Dict index out of range")

    @property
    def first_value(self):
        if self:
            for key in self:
                return self[key]
        else:
            raise IndexError("Dict index out of range")

    @property
    def first_key_or_none(self):
        return self.first_item if self else None

    
    def replace_key(self, old_key, new_key, inplace: bool = True):
        if inplace:
            self[new_key] = self.pop(old_key)
        else:
            new_dict = deepcopy(self)
            new_dict[new_key] = new_dict.pop(old_key)
            return new_dict
