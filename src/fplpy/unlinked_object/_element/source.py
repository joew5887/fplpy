from .model import T_model
from typing import TypeVar, Generic, Sequence, Any
from abc import ABC, abstractmethod


T_source = TypeVar("T_source", bound="DataSourceModel[Any]")


class DataSourceModel(ABC, Generic[T_model]):
    @abstractmethod
    def get(self) -> Sequence[T_model]: ...


"""
class APIDataSourceModel(DataSourceModel[T_model], ABC, Generic[T_model]):
    def get(self) -> Sequence[T_model]:
        data = self.__get_raw_data()
        
        # Define the expected fields for LabelModelBase
        expected_keys = {f.name for f in LabelModel.__dataclass_fields__.values()}

        required_data = []
        for item in data:
            item_filtered = filter_dict(item, list(expected_keys))
            required_data.append(LabelModel(**item_filtered))

        return required_data
    
    @abstractmethod
    def __get_raw_data(self) -> list[dict[str, Any]]: ...
"""
