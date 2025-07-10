from __future__ import annotations
from .._element.element import ElementWithID
from .model import ChipModel
from typing import TypeVar


T_chip = TypeVar("T_chip", bound="Chip")


class Chip(ElementWithID[ChipModel]):
    def __repr__(self) -> str:
        fields = [
            f"{type(self).get_id_field_name()}(ID)={self.id}",
            f"name='{self.value.name}'",
        ]
        fields_str = ", ".join(fields)

        return f"Chip({fields_str})"

    def __str__(self) -> str:
        return self.value.name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Chip):
            return self.value == other.value

        return False

    def __hash__(self) -> int:
        return hash(self.id)

    @staticmethod
    def get_id_field_name() -> str:
        return "id"
