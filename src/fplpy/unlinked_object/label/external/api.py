from ..source import LabelDataSource
from ..model import LabelModel
from ..object import Label
from ....util.external.api import call_api, get_url
from ....util.other import filter_dict
from ..repository import BaseLabelRepository
from typing import Sequence, Any


class LabelAPIDataSource(LabelDataSource):
    def get(self) -> Sequence[LabelModel]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))

        # Define the expected fields for LabelModelBase
        expected_keys = {f.name for f in LabelModel.__dataclass_fields__.values()}

        required_data = []
        for item in data["element_stats"]:
            item_filtered = filter_dict(item, list(expected_keys))
            required_data.append(LabelModel(**item_filtered))

        return required_data


class LabelAPI(BaseLabelRepository[Label]):
    def __init__(self) -> None:
        super().__init__(Label, LabelAPIDataSource())
