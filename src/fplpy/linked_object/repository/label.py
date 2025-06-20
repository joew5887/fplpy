from ..objects import LinkedLabel
from ...unlinked_object.label.repository import BaseLabelRepository
from ...unlinked_object.label.external.api import LabelAPIDataSource
from ..template import LinkedLabelTemplate


class LabelAPI(BaseLabelRepository[LinkedLabelTemplate]):
    def __init__(self) -> None:
        super().__init__(LinkedLabel, LabelAPIDataSource())