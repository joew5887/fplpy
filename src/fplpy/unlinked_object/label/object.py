from __future__ import annotations
from .._element.element import Element
from .model import LabelModel
from typing import TypeVar


T_label = TypeVar("T_label", bound="UnlinkedLabel")


class UnlinkedLabel(Element[LabelModel]):
    def __repr__(self) -> str:
        fields = [
            f"label='{self.value.label}'",
            f"name='{self.value.name}'",
        ]
        fields_str = ", ".join(fields)

        return f"Label({fields_str})"
    
    def __str__(self) -> str:
        return self.value.label
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, UnlinkedLabel):
            return self.value.label == other.value.label and self.value.name == other.value.name
    
        return False
    
    def __hash__(self) -> int:
        return hash((self.value.label, self.value.name))
