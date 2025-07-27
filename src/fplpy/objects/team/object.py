from __future__ import annotations
from .._element.element import ElementWithIDandCode
from .model import TeamModel
from typing import Hashable, TypeVar, Any


T_team = TypeVar("T_team", bound="Team")


class Team(ElementWithIDandCode[TeamModel]):
    def __repr__(self) -> str:
        fields = [
            f"ID={self.id}",
            f"CODE={self.code}",
            f"name='{self.value.name}'",
        ]
        fields_str = ", ".join(fields)

        return f"Team({fields_str})"

    def __str__(self) -> str:
        return self.value.name

    @property
    def id(self) -> int:
        return self.value.id
    
    @property
    def code(self) -> int:
        return self.value.code
    
    def values_to_hash_and_eq(self) -> tuple[Hashable, ...]:
        return (
            "Team",
            self.id,
            self.code,
        )
        
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Team":
        return cls(TeamModel(**data))
