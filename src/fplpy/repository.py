from .unlinked_object._element.repository import RepositoryWithID, Repository
from .linked_object.objects import LinkedEvent, LinkedFixture, LinkedLabel, \
    LinkedPlayer, LinkedPosition, LinkedTeam, LinkedGameSettings, LinkedPlayerSummary

from .unlinked_object.event.external.api import EventAPIDataSource
from .unlinked_object.fixture.external.api import FixtureAPIDataSource
from .unlinked_object.label.external.api import LabelAPIDataSource
from .unlinked_object.player.external.api import PlayerAPIDataSource
from .unlinked_object.position.external.api import PositionAPIDataSource
from .unlinked_object.team.external.api import TeamAPIDataSource
from .unlinked_object.game_settings.external.api import GameSettingsAPIDataSource
from .unlinked_object.player_summary.external.api import PlayerSummaryAPIDataSource

from .unlinked_object.fixture.external.github import FixtureGitHubDataSource
from .unlinked_object.player.external.github import PlayerGitHubDataSource
from .unlinked_object.team.external.github import TeamGitHubDataSource

EventAPI = RepositoryWithID(LinkedEvent, EventAPIDataSource())
FixtureAPI = RepositoryWithID(LinkedFixture, FixtureAPIDataSource())
LabelAPI = Repository(LinkedLabel, LabelAPIDataSource())
PlayerAPI = RepositoryWithID(LinkedPlayer, PlayerAPIDataSource())
PositionAPI = RepositoryWithID(LinkedPosition, PositionAPIDataSource())
TeamAPI = RepositoryWithID(LinkedTeam, TeamAPIDataSource())
GameSettingsAPI = Repository(LinkedGameSettings, GameSettingsAPIDataSource())


def PlayerSummaryAPI(player_id: int) -> Repository[LinkedPlayerSummary, PlayerSummaryAPIDataSource]:
    return Repository(LinkedPlayerSummary, PlayerSummaryAPIDataSource(player_id=player_id))


def FixtureGitHub(season: str) -> RepositoryWithID[LinkedFixture, FixtureGitHubDataSource]:
    return RepositoryWithID(LinkedFixture, FixtureGitHubDataSource(season=season))


def PlayerGitHub(season: str) -> RepositoryWithID[LinkedPlayer, PlayerGitHubDataSource]:
    return RepositoryWithID(LinkedPlayer, PlayerGitHubDataSource(season=season))


def TeamGitHub(season: str) -> RepositoryWithID[LinkedTeam, TeamGitHubDataSource]:
    return RepositoryWithID(LinkedTeam, TeamGitHubDataSource(season=season))
