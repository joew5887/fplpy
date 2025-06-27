from __future__ import annotations
from .._element.element import ElementWithID
from .model import EventModel
from datetime import datetime
from ...util.dt import string_to_datetime
from typing import TypeVar


T_event = TypeVar("T_event", bound="UnlinkedEvent")


class UnlinkedEvent(ElementWithID[EventModel]):
    def __repr__(self) -> str:
        fields = [
            f"{type(self).get_id_field_name()}(ID)={self.id}",
            f"name='{self.value.name}'",
            f"deadline_time='{self.value.deadline_time}'"
        ]
        fields_str = ", ".join(fields)

        return f"Event({fields_str})"

    def __str__(self) -> str:
        return self.value.name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, UnlinkedEvent):
            return self.id == other.id

        return False

    def __hash__(self) -> int:
        return hash(self.id)

    @staticmethod
    def get_id_field_name() -> str:
        return "id"

    @property
    def deadline_time(self) -> datetime:
        if self.value.deadline_time is None:
            return datetime.max

        return string_to_datetime(self.value.deadline_time)

    @property
    def has_started(self) -> bool:
        """Has the gameweek started?

        Uses `datetime.now()`.

        Returns
        -------
        bool
            True if gameweek has started, False otherwise.
        """
        return datetime.now() > self.deadline_time
