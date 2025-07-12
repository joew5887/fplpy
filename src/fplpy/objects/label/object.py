from __future__ import annotations
from .._element.element import Element
from .model import LabelModel
from typing import TypeVar, Hashable


T_label = TypeVar("T_label", bound="Label")


class Label(Element[LabelModel]):
    def __repr__(self) -> str:
        fields = [
            f"label='{self.value.label}'",
            f"name='{self.value.name}'",
        ]
        fields_str = ", ".join(fields)

        return f"Label({fields_str})"

    def __str__(self) -> str:
        return self.value.label

    def values_to_hash_and_eq(self) -> tuple[Hashable, ...]:
        return (
            "Label",
            self.value,
        )
