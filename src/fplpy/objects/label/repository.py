from .._element.repository import Repository
from .._element.source import DataSourceModel
from .model import LabelModel
from .object import T_label
from typing import Generic
from abc import ABC


class LabelRepository(Repository[T_label, DataSourceModel[LabelModel]], ABC, Generic[T_label]):
    pass
