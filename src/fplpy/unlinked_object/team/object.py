from __future__ import annotations
from .object_template import TeamTemplate
from typing import TypeVar


T_team = TypeVar("T_team", bound="TeamTemplate")


class Team(TeamTemplate):
    def __repr__(self) -> str:
        fields = [
            f"{Team.get_id_field_name()}(ID)={self.id}",
            f"name='{self.value.name}'",
        ]
        fields_str = ", ".join(fields)

        return f"{self.__class__.__name__}({fields_str})"
    
    def __str__(self) -> str:
        return self.value.name
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, TeamTemplate):
            return self.id == other.id and self.value.name == other.value.name
    
        return False
    
    def __hash__(self) -> int:
        return hash((self.id, self.value.name))
    
    @staticmethod
    def get_id_field_name() -> str:
        return "code"
