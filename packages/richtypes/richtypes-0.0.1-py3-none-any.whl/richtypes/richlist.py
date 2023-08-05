from copy import deepcopy
from typing import Callable, TypeVar

T = TypeVar("T")


class RichList(list):
    """Enhanced python list"""

    def __init__(self, *args: object) -> None:
        super().__init__(args)

    @property
    def length(self):
        """Returns the length of the list"""
        return len(self)

    @property
    def is_empty(self):
        """Returns true if the list is empty"""
        return len(self) == 0

    @property
    def is_not_empty(self):
        """Returns true if the list is not empty"""
        return len(self) > 0

    @property
    def first(self):
        """Returns the first element of the list"""
        if self:
            return self[0]
        else:
            raise IndexError("List index out of range")

    @property
    def first_or_none(self):
        """Returns the first element of the list or None"""
        return self.first if self else None

    @property
    def last(self):
        """Returns the last element of the list"""
        if self:
            return self[-1]
        else:
            raise IndexError("List index out of range")

    @property
    def last_or_none(self):
        """Returns the last element of the list or None"""
        return self.last if self else None

    def where(self, func: Callable[[T], bool], inplace: bool = True) -> "RichList":
        """Filters the list"""
        if inplace:
            self[:] = [item for item in self if func(item)]
        else:
            new_list = deepcopy(self)
            new_list[:] = [item for item in new_list if func(item)]
            return new_list

    def where_not(self, func: Callable[[T], bool], inplace: bool = True) -> "RichList":
        """Filters the list"""
        if inplace:
            self[:] = [item for item in self if not func(item)]
        else:
            new_list = deepcopy(self)
            new_list[:] = [item for item in new_list if not func(item)]
            return new_list

    def first_where(self, func: Callable[[T], bool]) -> T:
        """
        Returns the first element in the iterable for which the given function
        returns True.

        :param func: A Callable that takes an element from the iterable and
        returns a boolean value.
        :type func: Callable[[T], bool]

        :return: The first element in the iterable that satisfies the condition
        in `func`.
        :rtype: T
        """
        for item in self:
            if func(item):
                return item

    def last_where(self, func: Callable[[T], bool]) -> T:
        """
        Returns the last element in the iterable for which the given function
        returns True.

        :param func: A Callable that takes an element from the iterable and
        returns a boolean value.
        :type func: Callable[[T], bool]

        :return: The last element in the iterable that satisfies the condition
        in `func`.
        :rtype: T
        """
        for item in reversed(self):
            if func(item):
                return item
