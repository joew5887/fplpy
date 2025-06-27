from .unlinked_object._element.repository import RepositoryWithID, Repository
from .linked_object.objects import *

from .unlinked_object.event.repository import EventRepository

from .unlinked_object.event.external.api import EventAPIDataSource
from .unlinked_object.fixture.external.api import FixtureAPIDataSource
from .unlinked_object.label.external.api import LabelAPIDataSource
from .unlinked_object.player.external.api import PlayerAPIDataSource
from .unlinked_object.position.external.api import PositionAPIDataSource
from .unlinked_object.team.external.api import TeamAPIDataSource
from .unlinked_object.game_settings.external.api import GameSettingsAPIDataSource
from .unlinked_object.player_summary.external.api import PlayerSummaryAPIDataSource
from .unlinked_object.chip.external.api import ChipAPIDataSource

from .unlinked_object.fixture.external.github import FixtureGitHubDataSource
from .unlinked_object.player.external.github import PlayerGitHubDataSource
from .unlinked_object.team.external.github import TeamGitHubDataSource
from .unlinked_object.player_summary.external.github import PlayerSummaryGitHubDataSource

from .unlinked_object.event.external.local import EventLocalDataSource


def EventLocal2425(file_path: str) -> EventRepository[LinkedEvent, EventLocalDataSource]:
    return EventRepository(LinkedEvent, EventLocalDataSource(file_path=file_path))


EventAPI = EventRepository(LinkedEvent, EventAPIDataSource())
FixtureAPI = RepositoryWithID(LinkedFixture, FixtureAPIDataSource())
LabelAPI = Repository(LinkedLabel, LabelAPIDataSource())
PlayerAPI = RepositoryWithID(LinkedPlayer, PlayerAPIDataSource())
PositionAPI = RepositoryWithID(LinkedPosition, PositionAPIDataSource())
TeamAPI = RepositoryWithID(LinkedTeam, TeamAPIDataSource())
GameSettingsAPI = Repository(LinkedGameSettings, GameSettingsAPIDataSource())
ChipAPI = Repository(LinkedChip, ChipAPIDataSource())


def PlayerSummaryAPI(player_id: int) -> Repository[LinkedPlayerSummary, PlayerSummaryAPIDataSource]:
    return Repository(LinkedPlayerSummary, PlayerSummaryAPIDataSource(player_id=player_id))


def FixtureGitHub(season: str) -> RepositoryWithID[LinkedFixture, FixtureGitHubDataSource]:
    return RepositoryWithID(LinkedFixture, FixtureGitHubDataSource(season=season))


def PlayerGitHub(season: str) -> RepositoryWithID[LinkedPlayer, PlayerGitHubDataSource]:
    return RepositoryWithID(LinkedPlayer, PlayerGitHubDataSource(season=season))


def TeamGitHub(season: str) -> RepositoryWithID[LinkedTeam, TeamGitHubDataSource]:
    return RepositoryWithID(LinkedTeam, TeamGitHubDataSource(season=season))


def PlayerSummaryGitHub(season: str, player_name_formatted: str) -> Repository[LinkedPlayerSummary, PlayerSummaryGitHubDataSource]:
    return Repository(
        LinkedPlayerSummary,
        PlayerSummaryGitHubDataSource(season=season, player_name_formatted=player_name_formatted)
    )

"""
def get_player_repo(source: str, season: Optional[str] = None) -> RepositoryWithID:
    if source == "api":
        return RepositoryWithID(LinkedPlayer, PlayerAPIDataSource())
    elif (source == "github") and (season is not None):
        return RepositoryWithID(LinkedPlayer, PlayerGitHubDataSource(season))
    
    raise NotImplementedError
"""

