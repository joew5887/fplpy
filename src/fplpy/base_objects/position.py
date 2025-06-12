from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from .elements import Element
from ..external.api import FPLAPI


@dataclass(frozen=True, order=True, kw_only=True)
class Position(Element["Position"]):
    """Position for FPL player. E.g. 'Midfielder'.

    Replaces `player.element_type`.
    """
    STR_ATTR = "singular_name"

    id: int = field(repr=False)

    plural_name: str = field(hash=False, repr=False, compare=False)
    plural_name_short: str = field(hash=False, repr=False, compare=False)
    singular_name: str = field(compare=False)
    singular_name_short: str = field(repr=False, compare=False)
    squad_select: int = field(hash=False, repr=False, compare=False)
    squad_min_play: int = field(hash=False, repr=False, compare=False)
    squad_max_play: int = field(hash=False, repr=False, compare=False)
    ui_shirt_specific: bool = field(hash=False, repr=False, compare=False)
    sub_positions_locked: list[int] = field(hash=False, repr=False, compare=False)
    element_count: int = field(hash=False, repr=False, compare=False)
    
    @classmethod
    def from_dict_api(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        return element_args
    
    @classmethod
    def from_dict_vaastav(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        return element_args

    @classmethod
    def get_latest_external_data(cls, source: FPLAPI) -> list[dict[str, Any]]:
        return source.get_positions()

    @classmethod
    def get_by_name(cls, singular_name_short: str) -> Position:
        position = cls.get(singular_name_short=singular_name_short)

        return position[0]

    @classmethod
    def get_short_to_full_name_dict(cls) -> dict[str, Position]:
        """Get all positions, with the keys as the `singular_name_short`.

        Returns
        -------
        dict[str, Position]
            ```{"GKP": Goalkeeper, ..., "FWD": Forward}```
        """
        positions = cls.get_all()

        return {position.singular_name_short: position for position in positions}
