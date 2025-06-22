from __future__ import annotations
from .._element.element import ElementWithID
from .model import ChipModel
from datetime import datetime
from ...util.dt import string_to_datetime
from typing import TypeVar


T_chip = TypeVar("T_chip", bound="UnlinkedChip")


class UnlinkedChip(ElementWithID[ChipModel]):
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
        if isinstance(other, UnlinkedChip):
            return self.id == other.id and self.value.name == other.value.name

        return False

    def __hash__(self) -> int:
        return hash((self.id, self.value.name))

    @staticmethod
    def get_id_field_name() -> str:
        return "id"
