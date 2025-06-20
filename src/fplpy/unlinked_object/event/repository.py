from .object import T_event
from .source import EventDataSource
from .._element.repository import BaseRepositoryWithID
from typing import Generic
from abc import ABC


class BaseEventRepository(BaseRepositoryWithID[T_event, EventDataSource], ABC, Generic[T_event]): ...
