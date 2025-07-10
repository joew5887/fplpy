from .._element.repository import RepositoryWithID
from .._element.source import DataSourceModel
from .model import EventModel
from .object import T_event
from typing import Generic, Optional
from abc import ABC


class EventRepository(RepositoryWithID[T_event, DataSourceModel[EventModel]], ABC, Generic[T_event]):
    def get_next_event(self, event: T_event) -> Optional[T_event]:
        return self.get_by_id(event.id + 1)
    
    def get_previous_event(self, event: T_event) -> Optional[T_event]:
        return self.get_by_id(event.id - 1)
