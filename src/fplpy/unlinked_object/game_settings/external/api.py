from ..._element.source import APIDataSourceModel
from ....util.external.api import call_api, get_url
from ..model import GameSettingsModel
from typing import Any


class GameSettingsAPIDataSource(APIDataSourceModel[GameSettingsModel]):
    def __init__(self) -> None:
        super().__init__(GameSettingsModel)

    def _get_raw_data(self) -> list[dict[str, Any]]:
        data: dict[str, dict[str, Any]] = call_api(get_url("BOOTSTRAP-STATIC"))

        return [data["game_settings"]]
