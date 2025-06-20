from ..source import FixtureDataSource
from ..model import FixtureModel
from ..object import Fixture
from ....util.external.api import call_api, get_url
from ....util.other import filter_dict
from ..repository import BaseFixtureRepository
from typing import Sequence, Any, Type


class FixtureAPIDataSource(FixtureDataSource):
    def get(self) -> Sequence[FixtureModel]:
        data: list[dict[str, Any]] = call_api(get_url("FIXTURES"))

        # Define the expected fields for FixtureModelBase
        expected_keys = {f.name for f in FixtureModel.__dataclass_fields__.values()}

        required_data = []
        for item in data:
            item_filtered = filter_dict(item, list(expected_keys))
            required_data.append(FixtureModel(**item_filtered))

        return required_data


class FixtureAPI(BaseFixtureRepository[Fixture]):
    def __init__(self) -> None:
        super().__init__(Fixture, FixtureAPIDataSource())
