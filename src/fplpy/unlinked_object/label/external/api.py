from ..._element.source import APIDataSourceModel
from ....util.external.api import call_api, get_url
from ..model import LabelModel
from typing import Any


class LabelAPIDataSource(APIDataSourceModel[LabelModel]):
    def __init__(self) -> None:
        super().__init__(LabelModel)

    def _get_raw_data(self) -> list[dict[str, Any]]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))
        label_data = data["element_stats"]
        
        return label_data
