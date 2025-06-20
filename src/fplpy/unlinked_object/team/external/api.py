from ..._element.source import APIDataSourceModel
from ....util.external.api import call_api, get_url
from ..model import TeamModel
from typing import Any


class TeamAPIDataSource(APIDataSourceModel[TeamModel]):
    def __init__(self) -> None:
        super().__init__(TeamModel)

    def _get_raw_data(self) -> list[dict[str, Any]]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))
        
        return data["teams"]
