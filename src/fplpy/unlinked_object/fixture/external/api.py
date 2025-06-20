from ..._element.source import APIDataSourceModel
from ....util.external.api import call_api, get_url
from ..model import FixtureModel
from typing import Any


class FixtureAPIDataSource(APIDataSourceModel[FixtureModel]):
    def __init__(self) -> None:
        super().__init__(FixtureModel)

    def _get_raw_data(self) -> list[dict[str, Any]]:
        data: list[dict[str, Any]] = call_api(get_url("FIXTURES"))
        
        return data
