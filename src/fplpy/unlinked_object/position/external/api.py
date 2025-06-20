from ..source import PositionDataSource
from ..model import PositionModel
from ..object import Position
from ..repository import BasePositionRepository
from ....util.external.api import call_api, get_url
from ....util.other import filter_dict
from typing import Sequence, Any


class PositionAPIDataSource(PositionDataSource):
    def get(self) -> Sequence[PositionModel]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))

        # Define the expected fields for PositionModelBase
        expected_keys = {f.name for f in PositionModel.__dataclass_fields__.values()}

        required_data = []
        for item in data["element_types"]:
            item_filtered = filter_dict(item, list(expected_keys))
            required_data.append(PositionModel(**item_filtered))

        return required_data


class PositionAPI(BasePositionRepository[Position]):
    def __init__(self) -> None:
        super().__init__(Position, PositionAPIDataSource())
