from __future__ import annotations
from .object_template import PlayerTemplate
from typing import TypeVar


T_player = TypeVar("T_player", bound="PlayerTemplate")


class Player(PlayerTemplate):
    def __repr__(self) -> str:
        raise NotImplementedError
    
    def __str__(self) -> str:
        return self.value.web_name
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, PlayerTemplate):
            return self.id == other.id
    
        return False
    
    def __hash__(self) -> int:
        raise NotImplementedError
    
    @staticmethod
    def get_id_field_name() -> str:
        return "code"
