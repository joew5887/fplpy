from .object import T_label
from .._element.source import DataSourceModel
from .model import LabelModel
from .._element.repository import Repository
from typing import Generic
from abc import ABC


class BaseLabelRepository(Repository[T_label, DataSourceModel[LabelModel]], ABC, Generic[T_label]): ...
