from __future__ import annotations
from .._element.element import ElementWithID
from .model import FixtureModel
from typing import TypeVar


T_fixture = TypeVar("T_fixture", bound="UnlinkedFixture")


class UnlinkedFixture(ElementWithID[FixtureModel]):
    def __repr__(self) -> str:
        fields = [
            f"{type(self).get_id_field_name()}(ID)={self.id}",
            f"team_h={self.value.team_h}",
            f"team_a={self.value.team_a}",
            f"event={self.value.event}",
        ]
        fields_str = ", ".join(fields)

        return f"Fixture({fields_str})"
    
    def __str__(self) -> str:
        return f"{self.value.team_h} v {self.value.team_a}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, UnlinkedFixture):
            return self.value == other.value
        
        return False
    
    def __hash__(self) -> int:
        raise NotImplementedError
    
    @staticmethod
    def get_id_field_name() -> str:
        return "code"
