from __future__ import annotations
from .element_template import ElementTemplateWithID, ElementTemplate, ElementTemplateWithIDandCode
from .model import T_model
from abc import ABC, abstractmethod
from typing import Generic, Hashable, Any
from dataclasses import asdict


class Element(ElementTemplate[T_model], ABC, Generic[T_model]):
    value: T_model

    def __init__(self, attributes: T_model) -> None:
        self.value = attributes
        
    def __hash__(self) -> int:
        return hash(self.values_to_hash_and_eq())
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Element):
            return self.values_to_hash_and_eq() == other.values_to_hash_and_eq()

        return False
    
    def to_dict(self) -> dict[str, Any]:
        return asdict(self.value)

    @abstractmethod
    def values_to_hash_and_eq(self) -> tuple[Hashable, ...]:
        ...


class ElementWithID(Element[T_model], ElementTemplateWithID[T_model], ABC, Generic[T_model]):
    ...
    
    
class ElementWithIDandCode(Element[T_model], ElementTemplateWithIDandCode[T_model], ABC, Generic[T_model]):
    ...
