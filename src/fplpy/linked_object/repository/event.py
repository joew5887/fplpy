from ..objects import LinkedEvent
from ...unlinked_object.event.repository import BaseEventRepository
from ...unlinked_object.event.external.api import EventAPIDataSource


class EventAPI(BaseEventRepository[LinkedEvent]):
    def __init__(self) -> None:
        super().__init__(LinkedEvent, EventAPIDataSource())