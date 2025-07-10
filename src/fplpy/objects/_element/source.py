from .model import T_model
from typing import TypeVar, Generic, Sequence, Any, Type
from abc import ABC, abstractmethod
from ...util.other import filter_dict
from dataclasses import fields


T_source = TypeVar("T_source", bound="DataSourceModel[Any]")

SUPPORTED_SEASONS = (
    "2024-25",
    "2023-24",
    "2022-23"
)


class DataSourceModel(ABC, Generic[T_model]):
    @abstractmethod
    def get(self) -> Sequence[T_model]: ...

    @abstractmethod
    def _get_raw_data(self) -> Sequence[dict[str, Any]]: ...


class APIDataSourceModel(DataSourceModel[T_model], ABC, Generic[T_model]):
    def __init__(self, model_cls: Type[T_model]) -> None:
        self.__model_cls = model_cls

    @abstractmethod
    def _get_raw_data(self) -> list[dict[str, Any]]: ...

    def get(self) -> list[T_model]:
        data = self._get_raw_data()

        # Define the expected fields for LabelModelBase
        expected_keys = {f.name for f in self.__model_cls.__dataclass_fields__.values()}

        required_data = []
        for item in data:
            item_filtered = filter_dict(item, list(expected_keys))
            required_data.append(self.__model_cls(**item_filtered))

        return required_data


class GitHubDataSourceModel(DataSourceModel[T_model], ABC, Generic[T_model]):
    def __init__(self, model_cls: Type[T_model], season: str) -> None:
        self.__model_cls = model_cls

        if season not in SUPPORTED_SEASONS:
            raise ValueError(f"season not in {SUPPORTED_SEASONS}")
        self.__season = season

    @property
    def season(self) -> str:
        return self.__season

    @abstractmethod
    def _get_raw_data(self) -> list[dict[str, Any]]: ...

    def get(self) -> list[T_model]:
        data = self._get_raw_data()

        # Define the expected fields for LabelModelBase
        expected_keys = {f.name for f in self.__model_cls.__dataclass_fields__.values()}

        required_data = []
        for item in data:
            item_filtered = filter_dict(item, list(expected_keys))
            item_typed = coerce_types(self.__model_cls, item_filtered)  # csv has all values as string
            required_data.append(self.__model_cls(**item_typed))

        return required_data


def coerce_types(model_cls: Type[T_model], data: dict[str, Any]) -> dict[str, Any]:
    coerced: dict[str, Any] = {}
    for f in fields(model_cls):
        value = data.get(f.name)
        if (value is None) or (value == "None"):
            coerced[f.name] = None
        elif f.type == int:
            coerced[f.name] = int(value)
        elif f.type == float:
            coerced[f.name] = float(value)
        elif f.type == bool:
            coerced[f.name] = value.lower() == "true" if isinstance(value, str) else bool(value)
        elif f.type == list[dict[str, Any]]:
            coerced[f.name] = value if isinstance(value, list) else []
        else:
            coerced[f.name] = value
    return coerced
