from __future__ import annotations
from .._element.element import ElementWithID
from .model import EventModel
from datetime import datetime
from ...util.dt import string_to_datetime
from typing import TypeVar, Hashable, Any


T_event = TypeVar("T_event", bound="Event")


class Event(ElementWithID[EventModel]):
    def __repr__(self) -> str:
        fields = [
            f"ID={self.id}",
            f"name='{self.value.name}'",
            f"deadline_time='{self.value.deadline_time}'"
        ]
        fields_str = ", ".join(fields)

        return f"Event({fields_str})"

    def __str__(self) -> str:
        return self.value.name
    
    @property
    def id(self) -> int:
        return self.value.id

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
    
    def values_to_hash_and_eq(self) -> tuple[Hashable, ...]:
        return (
            "Event",
            self.id,
            self.value.name,
            self.value.deadline_time
        )
        
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Event":
        return cls(EventModel(**data))
