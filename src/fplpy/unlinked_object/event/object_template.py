from __future__ import annotations
from .._element.element import ElementWithID
from .model import EventModel
from datetime import datetime
from typing import TypeVar
from abc import ABC, abstractmethod


class EventTemplate(ElementWithID[EventModel], ABC):
    @property
    @abstractmethod
    def deadline_time(self) -> datetime: ...
    
    @property
    @abstractmethod
    def has_started(self) -> bool: ...
