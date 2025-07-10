from ..._element.source import GitHubDataSourceModel
from ..model import PlayerSummaryModel
from ....util.external.github import github_csv_to_dict, get_element_summary_url
from typing import Any


class PlayerSummaryGitHubDataSource(GitHubDataSourceModel[PlayerSummaryModel]):
    def __init__(self, season: str, player_name_formatted: str) -> None:
        super().__init__(PlayerSummaryModel, season)
        
        self.__player_name_formatted = player_name_formatted

    def _get_raw_data(self) -> list[dict[str, Any]]:
        url = get_element_summary_url(self.season, self.__player_name_formatted)
        data: list[dict[str, Any]] = github_csv_to_dict(url)

        return data
