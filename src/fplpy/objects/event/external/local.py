from ..._element.source import DataSourceModel
from ..model import EventModel
from ....util.other import filter_dict
from typing import Any
import json


class EventLocalDataSource(DataSourceModel[EventModel]):
    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path

    def get(self) -> list[EventModel]:
        data = self._get_raw_data()

        # Define the expected fields for LabelModelBase
        expected_keys = {f.name for f in EventModel.__dataclass_fields__.values()}

        required_data = []
        for item in data:
            item_filtered = filter_dict(item, list(expected_keys))
            required_data.append(EventModel(**item_filtered))

        return required_data

    def _get_raw_data(self) -> list[dict[str, Any]]:
        with open(self.__file_path, "r") as f:
            gameweek_data: list[dict[str, Any]] = json.load(f)

        return gameweek_data
