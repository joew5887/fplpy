from ..._element.source import GitHubDataSourceModel
from ..model import TeamModel
from ....util.external.github import get_vaastav_url, github_csv_to_dict
from typing import Any


class TeamGitHubDataSource(GitHubDataSourceModel[TeamModel]):
    def __init__(self, season: str) -> None:
        super().__init__(TeamModel, season)

    def _get_raw_data(self) -> list[dict[str, Any]]:
        url = get_vaastav_url("TEAMS", self.season)
        data: list[dict[str, Any]] = github_csv_to_dict(url)

        return data
