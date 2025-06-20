from ..source import EventDataSource
from ..model import EventModel
from ..object import Event
from ....util.external.api import call_api, get_url
from ....util.other import filter_dict
from ..repository import BaseEventRepository
from typing import Sequence, Any


class EventAPIDataSource(EventDataSource):
    def get(self) -> Sequence[EventModel]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))
        event_data = data["Events"]

        # Define the expected fields for EventModelBase
        expected_keys = {f.name for f in EventModel.__dataclass_fields__.values()}

        required_data = []
        for item in event_data:
            item_filtered = filter_dict(item, list(expected_keys))
            required_data.append(EventModel(**item_filtered))

        return required_data


class EventAPI(BaseEventRepository[Event]):
    def __init__(self) -> None:
        super().__init__(Event, EventAPIDataSource())
