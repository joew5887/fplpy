from __future__ import annotations
from .._element.element import ElementWithIDandCode
from .model import PlayerModel
from typing import TypeVar


T_player = TypeVar("T_player", bound="Player")


class Player(ElementWithIDandCode[PlayerModel]):
    def __repr__(self) -> str:
        fields = [
            f"code(ID)={self.id}",
            f"web_name='{self.value.web_name}'",
            f"team={self.value.team}",
            f"position={self.value.element_type}"
        ]
        fields_str = ", ".join(fields)

        return f"Player({fields_str})"

    def __str__(self) -> str:
        return self.value.web_name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Player):
            return self.id == other.id

        return False

    def __hash__(self) -> int:
        raise NotImplementedError

    @staticmethod
    def get_id_field_name() -> str:
        return "id"
    
    @staticmethod
    def get_code_field_name() -> str:
        return "code"
