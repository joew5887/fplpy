from .object import T_event
from .._element.source import DataSourceModel
from .model import EventModel
from .._element.repository import RepositoryWithID
from typing import Generic
from abc import ABC


class BaseEventRepository(RepositoryWithID[T_event, DataSourceModel[EventModel]], ABC, Generic[T_event]): ...
