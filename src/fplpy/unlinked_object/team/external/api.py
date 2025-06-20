from ..source import TeamDataSource
from ..model import TeamModel
from ..object import Team
from ....util.external.api import call_api, get_url
from ....util.other import filter_dict
from ..repository import BaseTeamRepository
from typing import Sequence, Any


class TeamAPIDataSource(TeamDataSource):
    def get(self) -> Sequence[TeamModel]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))
        team_data = data["teams"]
        processed_team_data = process_api_data(team_data, TeamModel)

        return processed_team_data


from typing import Type    
def process_api_data(data: list[dict[str, Any]], model_cls: Type[TeamModel]) -> list[TeamModel]:
    # Define the expected fields for TeamModelBase
    expected_keys = {f.name for f in model_cls.__dataclass_fields__.values()}

    required_data = []
    for item in data:
        item_filtered = filter_dict(item, list(expected_keys))
        required_data.append(TeamModel(**item_filtered))
        
    return required_data


class TeamAPI(BaseTeamRepository[Team]):
    def __init__(self) -> None:
        super().__init__(Team, TeamAPIDataSource())
