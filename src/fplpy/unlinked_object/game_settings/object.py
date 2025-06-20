from __future__ import annotations
from .._element.element import Element
from .model import GameSettingsModel
from typing import TypeVar


T_GameSettings = TypeVar("T_GameSettings", bound="UnlinkedGameSettings")


class UnlinkedGameSettings(Element[GameSettingsModel]):
    def __repr__(self) -> str:
        raise NotImplementedError
    
    def __str__(self) -> str:
        raise NotImplementedError
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError
    
    def __hash__(self) -> int:
        raise NotImplementedError