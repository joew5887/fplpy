from __future__ import annotations
from .model import T_model
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any


T = TypeVar("T")
T_element = TypeVar("T_element", bound="ElementTemplate[Any]")
T_element_with_id = TypeVar("T_element_with_id", bound="ElementTemplateWithID[Any]")
T_element_with_id_and_code = TypeVar("T_element_with_id_and_code", bound="ElementTemplateWithIDandCode[Any]")


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
    
    
class Serialisable(ABC):
    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        ...

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict[str, Any]) -> Any:
        ...


class HasID(ABC):
    @property
    @abstractmethod
    def id(self) -> int: ...
    

class HasCode(ABC):
    @property
    @abstractmethod
    def code(self) -> int: ...


class ElementTemplate(SingleArgumentInitialisable[T_model], Serialisable, Representable, Comparable, Hashable, ABC, Generic[T_model]):
    ...


class ElementTemplateWithID(ElementTemplate[T_model], HasID, ABC, Generic[T_model]):
    ...
    

class ElementTemplateWithIDandCode(ElementTemplateWithID[T_model], HasCode, ABC, Generic[T_model]):
    ...
