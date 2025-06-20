from ..._element.source import APIDataSourceModel
from ....util.external.api import call_api, get_url
from ..model import PlayerModel
from typing import Any


class PlayerAPIDataSource(APIDataSourceModel[PlayerModel]):
    def __init__(self) -> None:
        super().__init__(PlayerModel)

    def _get_raw_data(self) -> list[dict[str, Any]]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))
        Player_data = data["elements"]
        
        return Player_data
