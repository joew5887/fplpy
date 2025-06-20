from .unlinked_object._element.repository import RepositoryWithID, Repository
from .linked_object.objects import LinkedEvent, LinkedFixture, LinkedLabel, \
    LinkedPlayer, LinkedPosition, LinkedTeam

from .unlinked_object.event.external.api import EventAPIDataSource
from .unlinked_object.fixture.external.api import FixtureAPIDataSource
from .unlinked_object.label.external.api import LabelAPIDataSource
from .unlinked_object.player.external.api import PlayerAPIDataSource
from .unlinked_object.position.external.api import PositionAPIDataSource
from .unlinked_object.team.external.api import TeamAPIDataSource

from .unlinked_object.fixture.external.github import FixtureGitHubDataSource
from .unlinked_object.player.external.github import PlayerGitHubDataSource
from .unlinked_object.team.external.github import TeamGitHubDataSource

EventAPI = RepositoryWithID(LinkedEvent, EventAPIDataSource())

FixtureAPI = RepositoryWithID(LinkedFixture, FixtureAPIDataSource())
FixtureGitHub = lambda season: RepositoryWithID(LinkedFixture, FixtureGitHubDataSource(season=season))

LabelAPI = Repository(LinkedLabel, LabelAPIDataSource())

PlayerAPI = RepositoryWithID(LinkedPlayer, PlayerAPIDataSource())
PlayerGitHub = lambda season: RepositoryWithID(LinkedPlayer, PlayerGitHubDataSource(season=season))

PositionAPI = RepositoryWithID(LinkedPosition, PositionAPIDataSource())

TeamAPI = RepositoryWithID(LinkedTeam, TeamAPIDataSource())
TeamGitHub = lambda season: RepositoryWithID(LinkedTeam, TeamGitHubDataSource(season=season))