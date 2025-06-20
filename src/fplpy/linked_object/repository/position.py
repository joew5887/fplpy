from ..objects import LinkedPosition
from ...unlinked_object.position.repository import BasePositionRepository
from ...unlinked_object.position.external.api import PositionAPIDataSource
from ..template import LinkedPositionTemplate


class PositionAPI(BasePositionRepository[LinkedPositionTemplate]):
    def __init__(self) -> None:
        super().__init__(LinkedPosition, PositionAPIDataSource())