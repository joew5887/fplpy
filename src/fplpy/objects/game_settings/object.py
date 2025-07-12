from __future__ import annotations
from .._element.element import Element
from .model import GameSettingsModel
from typing import Any, TypeVar


T_GameSettings = TypeVar("T_GameSettings", bound="GameSettings")


class GameSettings(Element[GameSettingsModel]):
    def __repr__(self) -> str:
        return "GameSettings(...)"

    def __str__(self) -> str:
        return "Game Settings"
    
    def values_to_hash_and_eq(self) -> tuple[Any, ...]:
        return (
            "GameSettings",
            self.value,
        )
