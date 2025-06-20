from ..._element.source import GitHubDataSourceModel
from ..model import PlayerModel
from ....util.external.github import get_vaastav_url, github_csv_to_dict
from typing import Any


class PlayerGitHubDataSource(GitHubDataSourceModel[PlayerModel]):
    def __init__(self, season: str) -> None:
        super().__init__(PlayerModel, season)

    def _get_raw_data(self) -> list[dict[str, Any]]:
        url = get_vaastav_url("PLAYERS", self.season)
        data: list[dict[str, Any]] = github_csv_to_dict(url)
        
        return data
