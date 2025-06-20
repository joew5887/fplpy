from __future__ import annotations
from .._element.element import ElementWithID
from .model import PositionModel
from typing import TypeVar


T_position = TypeVar("T_position", bound="UnlinkedPosition")


class UnlinkedPosition(ElementWithID[PositionModel]):
    def __repr__(self) -> str:
        fields = [
            f"id(ID)={self.id}",
            f"singular_name='{self.value.singular_name}'",
            f"singular_name_short='{self.value.singular_name_short}'"
        ]
        fields_str = ", ".join(fields)

        return f"Position({fields_str})"
    
    def __str__(self) -> str:
        return self.value.singular_name
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, UnlinkedPosition):
            return self.id == other.id and self.value.singular_name == other.value.singular_name
    
        return False
    
    def __hash__(self) -> int:
        return hash((self.id, self.value.singular_name))
    
    @staticmethod
    def get_id_field_name() -> str:
        return "id"
