from collections.abc import MutableSequence
from typing import Generic, Iterable, TypeVar
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

    def __getitem__(self, index: int) -> E:
        return self.__data[index]

    def __setitem__(self, index: int, value: E) -> None:
        self._check_type(value)
        if value in self.__data:
            raise ValueError("Duplicates not allowed")
        self.__data[index] = value

    def __delitem__(self, index: int) -> None:
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