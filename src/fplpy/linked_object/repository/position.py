from ..objects import LinkedPosition
from ...unlinked_object.position.repository import BasePositionRepository
from ...unlinked_object.position.external.api import PositionAPIDataSource


class PositionAPI(BasePositionRepository[LinkedPosition]):
    def __init__(self) -> None:
        super().__init__(LinkedPosition, PositionAPIDataSource())