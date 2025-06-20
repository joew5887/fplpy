from ..objects import LinkedTeam
from ...unlinked_object.team.repository import BaseTeamRepository
from ...unlinked_object.team.external.api import TeamAPIDataSource
from ...unlinked_object.team.external.github import TeamGitHubDataSource
from ..template import LinkedTeamTemplate


class TeamAPI(BaseTeamRepository[LinkedTeamTemplate]):
    def __init__(self) -> None:
        super().__init__(LinkedTeam, TeamAPIDataSource())
        
        
class TeamGitHub(BaseTeamRepository[LinkedTeamTemplate]):
    def __init__(self, season: str = "2024-25") -> None:
        super().__init__(LinkedTeam, TeamGitHubDataSource(season=season))
