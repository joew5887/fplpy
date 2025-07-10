from ..._element.source import GitHubDataSourceModel
from ..model import FixtureModel
from ....util.external.github import get_vaastav_url, github_csv_to_dict
from typing import Any


class FixtureGitHubDataSource(GitHubDataSourceModel[FixtureModel]):
    def __init__(self, season: str) -> None:
        super().__init__(FixtureModel, season)

    def _get_raw_data(self) -> list[dict[str, Any]]:
        url = get_vaastav_url("FIXTURES", self.__season)
        data: list[dict[str, Any]] = github_csv_to_dict(url)

        return data
