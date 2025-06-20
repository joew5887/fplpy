from ..objects import LinkedLabel
from ...unlinked_object.label.repository import BaseLabelRepository
from ...unlinked_object.label.external.api import LabelAPIDataSource


class LabelAPI(BaseLabelRepository[LinkedLabel]):
    def __init__(self) -> None:
        super().__init__(LinkedLabel, LabelAPIDataSource())