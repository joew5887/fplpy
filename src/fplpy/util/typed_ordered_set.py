from __future__ import annotations
from collections.abc import MutableSequence
from typing import Generic, Iterable, TypeVar, overload
from random import choice


E = TypeVar("E")


class TypedOrderedSet(MutableSequence[E], Generic[E]):
    __data: list[E]
    __expected_type: type | None

    def __init__(self, iterable: Iterable[E]) -> None:
        self.__data = []
        self.__expected_type = None
        
        for item in iterable:
            self.append(item)
            
    def __eq__(self, other: object) -> bool:
        if isinstance(other, TypedOrderedSet):
            return self.__data == other.to_list()
        
        raise NotImplementedError
    
    @overload
    def __getitem__(self, index: int) -> E: ...
    
    @overload
    def __getitem__(self, index: slice) -> TypedOrderedSet[E]: ...

    def __getitem__(self, index: int | slice) -> E | TypedOrderedSet[E]:
        if isinstance(index, slice):
            return TypedOrderedSet(self.__data[index])

        return self.__data[index]
    
    @overload
    def __setitem__(self, index: int, value: E) -> None: ...
    
    @overload
    def __setitem__(self, index: slice, value: Iterable[E]) -> None: ...

    def __setitem__(self, index: int | slice, value: E | Iterable[E]) -> None:
        if isinstance(index, int):
            if isinstance(value, Iterable):
                raise TypeError(f"Expected {type(value)}, got Iterable")

            # Checks
            self._check_type(value)
            if value in self.__data:
                raise ValueError("Duplicates not allowed")

            self.__data[index] = value
        
        elif isinstance(index, slice):
            if not isinstance(value, Iterable):  # Ensure iterable for slices
                raise TypeError(f"Expected Iterable, got {type(value)}")

            values = list(value)
            for v in values:
                self._check_type(v)

            if any(v in self.__data for v in values):  # Prevent duplicates
                raise ValueError("Duplicates not allowed in slice assignment")

            if len(values) != len(self.__data[index]):  # Enforce length match
                raise ValueError("Slice assignment length mismatch")

            self.__data[index] = values  # Assign sliced values correctly

    @overload
    def __delitem__(self, index: int) -> None: ...
    
    @overload
    def __delitem__(self, index: slice) -> None: ...

    def __delitem__(self, index: int | slice) -> None:
        del self.__data[index]

    def __len__(self) -> int:
        return len(self.__data)
    
    @property
    def is_empty(self) -> bool:
        return self.__data == []

    def insert(self, index: int, value: E) -> None:
        self._check_type(value)
        if value in self.__data:
            raise ValueError("Duplicates not allowed")
        self.__data.insert(index, value)

    def _check_type(self, value: E) -> None:
        if self.__expected_type is None:
            self.__expected_type = type(value)
            return
        
        if not isinstance(value, self.__expected_type):
            raise TypeError(f"Expected type {self.__expected_type}")

    def to_list(self) -> list[E]:
        return self.__data.copy()
    
    def get_random(self) -> E:
        return choice(self.__data)
    
    
if __name__ == "__main__":
    data = [1, 2]
    y = TypedOrderedSet(data)
    x = TypedOrderedSet(data)
    print(x == y)
