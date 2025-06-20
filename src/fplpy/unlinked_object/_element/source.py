from .model import T_model
from typing import TypeVar, Generic, Sequence, Any
from abc import ABC, abstractmethod


T = TypeVar("T")
T_source = TypeVar("T_source", bound="DataSource[Any]")


class DataSource(ABC, Generic[T]):
    @abstractmethod
    def get(self) -> T: ...
    

class DataSourceSequence(DataSource[Sequence[T]], ABC, Generic[T]): ...


class ModelDataSource(DataSourceSequence[T_model], ABC, Generic[T_model]): ...
