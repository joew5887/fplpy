from __future__ import annotations
from .._element.element import Element
from .model import PlayerSummaryModel
from typing import TypeVar, Hashable
from datetime import datetime
from ...util.dt import string_to_datetime


T_player_summary = TypeVar("T_player_summary", bound="PlayerSummary")


class PlayerSummary(Element[PlayerSummaryModel]):
    def __repr__(self) -> str:
        fields = [
            f"element='{self.value.element}'",
            f"fixture={self.value.fixture}",
        ]
        fields_str = ", ".join(fields)

        return f"PlayerSummary({fields_str})"
    
    @property
    def kickoff_time(self) -> datetime:
        return string_to_datetime(self.value.kickoff_time)

    def __str__(self) -> str:
        return repr(self)

    def values_to_hash_and_eq(self) -> tuple[Hashable, ...]:
        return (
            "PlayerSummary",
            self.value.element,
            self.value.fixture,
        )