from __future__ import annotations
from .._element.element import Element
from .model import PlayerSummaryModel
from typing import TypeVar


T_player_summary = TypeVar("T_player_summary", bound="PlayerSummary")


class PlayerSummary(Element[PlayerSummaryModel]):
    def __repr__(self) -> str:
        return self.value.kickoff_time

    def __str__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __hash__(self) -> int:
        raise NotImplementedError