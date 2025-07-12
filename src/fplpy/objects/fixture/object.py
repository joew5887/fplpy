from __future__ import annotations
from .._element.element import ElementWithIDandCode
from .model import FixtureModel
from typing import Hashable, TypeVar


T_fixture = TypeVar("T_fixture", bound="Fixture")


class Fixture(ElementWithIDandCode[FixtureModel]):
    def __repr__(self) -> str:
        fields = [
            f"ID={self.id}",
            f"CODE={self.code}",
            f"team_h={self.value.team_h}",
            f"team_a={self.value.team_a}",
            f"event={self.value.event}",
        ]
        fields_str = ", ".join(fields)

        return f"Fixture({fields_str})"

    def __str__(self) -> str:
        if self.value.finished:
            return f"(Team {self.value.team_h}) {self.value.team_h_score} - {self.value.team_a_score} (Team {self.value.team_a})"

        return f"Team {self.value.team_h} v Team {self.value.team_a}"
    
    def values_to_hash_and_eq(self) -> tuple[Hashable, ...]:
        return (
            "Fixture",
            self.id,
            self.code,
            self.value.team_h,
            self.value.team_a,
        )

    @property
    def id(self) -> int:
        return self.value.id
    
    @property
    def code(self) -> int:
        return self.value.code
