from __future__ import annotations
from .object_template import LabelTemplate
from typing import TypeVar


T_label = TypeVar("T_label", bound="LabelTemplate")


class Label(LabelTemplate):
    def __repr__(self) -> str:
        fields = [
            f"label={self.value.label}",
            f"name={self.value.name}",
        ]
        fields_str = ", ".join(fields)

        return f"{self.__class__.__name__}({fields_str})"
    
    def __str__(self) -> str:
        return self.value.name
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, LabelTemplate):
            return self.value.label == other.value.label and self.value.name == other.value.name
    
        return False
    
    def __hash__(self) -> int:
        return hash((self.value.label, self.value.name))
