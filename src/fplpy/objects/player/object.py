from __future__ import annotations
from .._element.element import ElementWithIDandCode
from .model import PlayerModel
from typing import Hashable, TypeVar, Any
from datetime import datetime


T_player = TypeVar("T_player", bound="Player")


class Player(ElementWithIDandCode[PlayerModel]):
    def __repr__(self) -> str:
        fields = [
            f"ID={self.id}",
            f"CODE={self.code}",
            f"web_name='{self.value.web_name}'",
            f"team={self.value.team}",
            f"position={self.value.element_type}"
        ]
        fields_str = ", ".join(fields)

        return f"Player({fields_str})"

    def __str__(self) -> str:
        return self.value.web_name

    @property
    def id(self) -> int:
        return self.value.id
    
    @property
    def team_join_date(self) -> datetime:
        if self.value.team_join_date is None:
            return datetime.max

        return datetime.strptime(self.value.team_join_date, "%Y-%m-%d")
    
    @property
    def code(self) -> int:
        return self.value.code
    
    def values_to_hash_and_eq(self) -> tuple[Hashable, ...]:
        return (
            "Player",
            self.id,
            self.code,
        )
        
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Player":
        return cls(PlayerModel(**data))
