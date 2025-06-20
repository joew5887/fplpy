from __future__ import annotations
from .object_template import FixtureTemplate
from typing import TypeVar


T_fixture = TypeVar("T_fixture", bound="FixtureTemplate")


class Fixture(FixtureTemplate):
    def __repr__(self) -> str:
        fields = [
            f"{Fixture.get_id_field_name()}(ID)={self.id}",
            f"team_h={self.value.team_h}",
            f"team_a={self.value.team_a}",
            f"event={self.value.event}",
        ]
        fields_str = ", ".join(fields)

        return f"{self.__class__.__name__}({fields_str})"
    
    def __str__(self) -> str:
        return f"{self.value.team_h} v {self.value.team_a}"
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError
    
    def __hash__(self) -> int:
        raise NotImplementedError
    
    @staticmethod
    def get_id_field_name() -> str:
        return "code"
