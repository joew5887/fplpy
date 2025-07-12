from __future__ import annotations
from .source import T_source
from abc import ABC
from typing import Generic, Callable, Optional, Type
from .element_template import T_element_with_id, T_element, \
    T_element_with_id_and_code


class Repository(ABC, Generic[T_element, T_source]):
    def __init__(self, element_cls: Type[T_element], source: T_source) -> None:
        self.__model_wrapper_cls = element_cls
        self.__source = source

    def get_all(self) -> list[T_element]:
        return [self.__model_wrapper_cls(item) for item in self.__source.get()]

    def get_filtered(self, filter_fn: Callable[[T_element], bool]) -> list[T_element]:
        return [item for item in self.get_all() if filter_fn(item)]


class RepositoryWithID(Repository[T_element_with_id, T_source], ABC, Generic[T_element_with_id, T_source]):
    def get_by_id(self, unique_id: int) -> Optional[T_element_with_id]:
        res = self.get_filtered(lambda x: x.id == unique_id)

        if len(res) == 1:
            return res[0]
        
        if len(res) == 0:
            return None

        raise ValueError(f"get_by_id() expected 1 or 0 results, obtained {len(res)} results")


class RepositoryWithIDandCode(RepositoryWithID[T_element_with_id_and_code, T_source], ABC, Generic[T_element_with_id_and_code, T_source]):
    def get_by_code(self, code: int) -> Optional[T_element_with_id_and_code]:
        res = self.get_filtered(lambda x: x.code == code)

        if len(res) == 1:
            return res[0]
        
        if len(res) == 0:
            return None

        raise ValueError(f"get_by_code() expected 1 or 0 results, obtained {len(res)} results")
