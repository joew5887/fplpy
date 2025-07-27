from __future__ import annotations
from .._element.element import Element
from .model import PlayerHistoryModel
from typing import TypeVar, Hashable, Any


T_player_history = TypeVar("T_player_history", bound="PlayerHistory")


class PlayerHistory(Element[PlayerHistoryModel]):
    def __repr__(self) -> str:
        fields = [
            f"season='{self.value.season_name}'",
            f"player_code={self.value.element_code}",
        ]
        fields_str = ", ".join(fields)

        return f"PlayerHistory({fields_str})"

    def __str__(self) -> str:
        return repr(self)

    def values_to_hash_and_eq(self) -> tuple[Hashable, ...]:
        return (
            "PlayerHistory",
            self.value.element_code,
            self.value.season_name,
        )
        
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PlayerHistory":
        return cls(PlayerHistoryModel(**data))
