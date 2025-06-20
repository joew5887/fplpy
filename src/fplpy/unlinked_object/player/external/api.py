from ..source import PlayerDataSource
from ..model import PlayerModel
from ..object import Player
from ....util.external.api import call_api, get_url
from ....util.other import filter_dict
from ..repository import BasePlayerRepository
from typing import Sequence, Any


class PlayerAPIDataSource(PlayerDataSource):
    def get(self) -> Sequence[PlayerModel]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))

        # Define the expected fields for PlayerModelBase
        expected_keys = {f.name for f in PlayerModel.__dataclass_fields__.values()}

        required_data = []
        for item in data["elements"]:
            item_filtered = filter_dict(item, list(expected_keys))
            required_data.append(PlayerModel(**item_filtered))

        return required_data


class PlayerAPI(BasePlayerRepository[Player]):
    def __init__(self) -> None:
        super().__init__(Player, PlayerAPIDataSource())
