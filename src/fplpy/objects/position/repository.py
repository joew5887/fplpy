from .._element.repository import RepositoryWithID
from .._element.source import DataSourceModel
from .model import PositionModel
from .object import T_position
from typing import Generic
from abc import ABC


class PositionRepository(RepositoryWithID[T_position, DataSourceModel[PositionModel]], ABC, Generic[T_position]):
    pass
