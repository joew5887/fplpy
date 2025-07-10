from __future__ import annotations
from .model import T_model
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any

# Type Variables
T = TypeVar("T")
T_element = TypeVar("T_element", bound="ElementTemplate[Any]")
T_element_with_id = TypeVar("T_element_with_id", bound="ElementTemplateWithID[Any]")


class SingleArgumentInitialisable(ABC, Generic[T]):
    @abstractmethod
    def __init__(self, attr: T) -> None: ...


class Representable(ABC):
    @abstractmethod
    def __repr__(self) -> str: ...

    @abstractmethod
    def __str__(self) -> str: ...


class Comparable(ABC):
    @abstractmethod
    def __eq__(self, other: object) -> bool: ...


class Hashable(ABC):
    @abstractmethod
    def __hash__(self) -> int: ...


class HasID(ABC):
    @property
    @abstractmethod
    def id(self) -> int: ...

    @staticmethod
    @abstractmethod
    def get_id_field_name() -> str: ...


class ElementTemplate(SingleArgumentInitialisable[T_model], Representable, Comparable, Hashable, ABC, Generic[T_model]):
    ...


class ElementTemplateWithID(ElementTemplate[T_model], HasID, ABC, Generic[T_model]):
    ...
