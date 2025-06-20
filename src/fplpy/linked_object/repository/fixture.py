from ..objects import LinkedFixture
from ...unlinked_object.fixture.repository import BaseFixtureRepository
from ...unlinked_object.fixture.external.api import FixtureAPIDataSource
from ...unlinked_object.fixture.external.github import FixtureGitHubDataSource


class FixtureAPI(BaseFixtureRepository[LinkedFixture]):
    def __init__(self) -> None:
        super().__init__(LinkedFixture, FixtureAPIDataSource())
        

class FixtureGitHub(BaseFixtureRepository[LinkedFixture]):
    def __init__(self, season: str = "2024-25") -> None:
        super().__init__(LinkedFixture, FixtureGitHubDataSource(season=season))