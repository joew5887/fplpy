from __future__ import annotations
from .._element.element import ElementWithID
from .model import ChipModel
from typing import Hashable, TypeVar, Any


T_chip = TypeVar("T_chip", bound="Chip")


class Chip(ElementWithID[ChipModel]):
    def __repr__(self) -> str:
        fields = [
            f"ID={self.id}",
            f"name='{self.value.name}'",
        ]
        fields_str = ", ".join(fields)

        return f"Chip({fields_str})"

    def __str__(self) -> str:
        return self.value.name
    
    @property
    def id(self) -> int:
        return self.value.id
    
    def values_to_hash_and_eq(self) -> tuple[Hashable, ...]:
        return (
            "Chip",
            self.id,
            self.value.name,
        )

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Chip":
        return cls(ChipModel(**data))
