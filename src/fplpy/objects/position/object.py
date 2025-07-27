from __future__ import annotations
from .._element.element import ElementWithID
from .model import PositionModel
from typing import TypeVar, Hashable, Any


T_position = TypeVar("T_position", bound="Position")


class Position(ElementWithID[PositionModel]):
    def __repr__(self) -> str:
        fields = [
            f"ID={self.id}",
            f"singular_name='{self.value.singular_name}'",
            f"singular_name_short='{self.value.singular_name_short}'"
        ]
        fields_str = ", ".join(fields)

        return f"Position({fields_str})"

    def __str__(self) -> str:
        return self.value.singular_name

    @property
    def id(self) -> int:
        return self.value.id
    
    def values_to_hash_and_eq(self) -> tuple[Hashable, ...]:
        return (
            "Position",
            self.id,
            self.value.plural_name,
            self.value.plural_name_short,
            self.value.singular_name,
            self.value.singular_name_short,
        )
        
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Position":
        return cls(PositionModel(**data))
