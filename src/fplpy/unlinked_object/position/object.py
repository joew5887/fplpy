from __future__ import annotations
from .object_template import PositionTemplate
from typing import TypeVar


T_position = TypeVar("T_position", bound="PositionTemplate")


class Position(PositionTemplate):
    def __repr__(self) -> str:
        fields = [
            f"id={self.id}",
            f"singular_name={self.value.singular_name}",
            f"singular_name_short={self.value.singular_name_short})"
        ]
        fields_str = ", ".join(fields)

        return f"{self.__class__.__name__}({fields_str})"
    
    def __str__(self) -> str:
        return self.value.singular_name
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, PositionTemplate):
            return self.id == other.id and self.value.singular_name == other.value.singular_name
    
        return False
    
    def __hash__(self) -> int:
        return hash((self.id, self.value.singular_name))
    
    @staticmethod
    def get_id_field_name() -> str:
        return "id"
