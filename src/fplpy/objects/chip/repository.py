from .._element.repository import Repository
from .._element.source import DataSourceModel
from .model import ChipModel
from .object import T_chip
from typing import Generic
from abc import ABC


class ChipRepository(Repository[T_chip, DataSourceModel[ChipModel]], ABC, Generic[T_chip]):
    pass
