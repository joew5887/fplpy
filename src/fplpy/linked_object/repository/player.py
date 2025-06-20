from ..objects import LinkedPlayer
from ...unlinked_object.player.repository import BasePlayerRepository
from ...unlinked_object.player.external.api import PlayerAPIDataSource
from ...unlinked_object.player.external.github import PlayerGitHubDataSource
from ..template import LinkedPlayerTemplate


class PlayerAPI(BasePlayerRepository[LinkedPlayerTemplate]):
    def __init__(self) -> None:
        super().__init__(LinkedPlayer, PlayerAPIDataSource())
        

class PlayerGitHub(BasePlayerRepository[LinkedPlayerTemplate]):
    def __init__(self, season: str = "2024-25") -> None:
        super().__init__(LinkedPlayer, PlayerGitHubDataSource(season=season))