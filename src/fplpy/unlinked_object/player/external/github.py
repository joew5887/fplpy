from ..source import PlayerDataSource
from ..model import PlayerModel
from ..object import Player
from ....util.external.github import get_vaastav_url, github_csv_to_dict
from ..repository import BasePlayerRepository
from ..._element.model import Model
from typing import Sequence, Any, Type


class PlayerGitHubDataSource(PlayerDataSource):
    def __init__(self, season: str = "2024-25") -> None:
        self.__season = season

    def get(self) -> Sequence[PlayerModel]:
        url = get_vaastav_url("PLAYERS", self.__season)
        data: list[dict[str, Any]] = github_csv_to_dict(url)

        # Define the expected fields for PlayerModelBase
        expected_keys = {f.name for f in PlayerModel.__dataclass_fields__.values()}

        required_data = []
        for item in data:
            item_filtered = filter_dict(item, list(expected_keys))
            item_typed = coerce_types(PlayerModel, item_filtered)  # csv has all values as string
            required_data.append(PlayerModel(**item_typed))

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
            if value == "None":
                coerced[f.name] = 0.0
            else:
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


class PlayerGitHub(BasePlayerRepository[Player]):
    def __init__(self, season: str = "2024-25") -> None:
        super().__init__(Player, PlayerGitHubDataSource(season=season))
