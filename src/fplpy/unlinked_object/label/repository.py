from .object import T_label
from .source import LabelDataSource
from .._element.repository import BaseRepository
from typing import Generic
from abc import ABC


class BaseLabelRepository(BaseRepository[T_label, LabelDataSource], ABC, Generic[T_label]): ...
