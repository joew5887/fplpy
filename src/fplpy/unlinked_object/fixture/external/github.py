from ..source import FixtureDataSource
from ..model import FixtureModel
from ..object import Fixture
from ....util.external.github import get_vaastav_url, github_csv_to_dict
from ..repository import BaseFixtureRepository
from ..._element.model import Model
from typing import Sequence, Any, Type


class FixtureGitHubDataSource(FixtureDataSource):
    def __init__(self, season: str = "2024-25") -> None:
        super().__init__()
        self.__season = season

    def get(self) -> Sequence[FixtureModel]:
        url = get_vaastav_url("FIXTURES", self.__season)
        data: list[dict[str, Any]] = github_csv_to_dict(url)

        # Define the expected fields for FixtureModelBase
        expected_keys = {f.name for f in FixtureModel.__dataclass_fields__.values()}

        required_data = []
        for item in data:
            item_filtered = filter_dict(item, list(expected_keys))
            item_typed = coerce_types(FixtureModel, item_filtered)  # csv has all values as string
            required_data.append(FixtureModel(**item_typed))

        return required_data
    
    
from dataclasses import fields

def coerce_types(model_cls: Type[Model], data: dict[str, Any]) -> dict[str, Any]:
    coerced: dict[str, Any] = {}
    for f in fields(model_cls):
        value = data.get(f.name)
        if value is None:
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
    

def filter_dict(data: dict[str, Any], allowed_keys: list[str]) -> dict[str, Any]:
    """Filter the dictionary to only include allowed keys."""
    return {key: data[key] for key in allowed_keys if key in data}


class FixtureGitHub(BaseFixtureRepository[Fixture]):
    def __init__(self, season: str = "2024-25") -> None:
        super().__init__(Fixture, FixtureGitHubDataSource(season=season))
