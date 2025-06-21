from __future__ import annotations
from .._element.element import ElementWithID
from .model import TeamModel
from typing import TypeVar


T_team = TypeVar("T_team", bound="UnlinkedTeam")


class UnlinkedTeam(ElementWithID[TeamModel]):
    def __repr__(self) -> str:
        fields = [
            f"{type(self).get_id_field_name()}(ID)={self.id}",
            f"name='{self.value.name}'",
        ]
        fields_str = ", ".join(fields)

        return f"Team({fields_str})"

    def __str__(self) -> str:
        return self.value.name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, UnlinkedTeam):
            return self.id == other.id and self.value.name == other.value.name

        return False

    def __hash__(self) -> int:
        return hash((self.id, self.value.name))

    @staticmethod
    def get_id_field_name() -> str:
        return "code"
