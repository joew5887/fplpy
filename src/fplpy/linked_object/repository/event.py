from ..objects import LinkedEvent
from ...unlinked_object.event.repository import BaseEventRepository
from ...unlinked_object.event.external.api import EventAPIDataSource
from ..template import LinkedEventTemplate


class EventAPI(BaseEventRepository[LinkedEventTemplate]):
    def __init__(self) -> None:
        super().__init__(LinkedEvent, EventAPIDataSource())