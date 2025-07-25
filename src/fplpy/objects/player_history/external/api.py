from ..._element.source import APIDataSourceModel
from ....util.external.api import call_api, get_element_summary_url
from ..model import PlayerHistoryModel
from typing import Any


class PlayerHistoryAPIDataSource(APIDataSourceModel[PlayerHistoryModel]):
    def __init__(self, player_id: int) -> None:
        super().__init__(PlayerHistoryModel)
        
        self.__player_id = player_id

    def _get_raw_data(self) -> list[dict[str, Any]]:
        url = get_element_summary_url(self.__player_id)
        data: dict[str, list[dict[str, Any]]] = call_api(url)

        return data["history_past"]
