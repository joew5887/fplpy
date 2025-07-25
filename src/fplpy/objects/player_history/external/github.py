from ..._element.source import GitHubDataSourceModel
from ..model import PlayerHistoryModel
from ....util.external.github import github_csv_to_dict, get_element_history_url
from typing import Any


class PlayerHistoryGitHubDataSource(GitHubDataSourceModel[PlayerHistoryModel]):
    def __init__(self, season: str, player_name_formatted: str) -> None:
        super().__init__(PlayerHistoryModel, season)
        
        self.__player_name_formatted = player_name_formatted

    def _get_raw_data(self) -> list[dict[str, Any]]:
        url = get_element_history_url(self.season, self.__player_name_formatted)
        
        data: list[dict[str, Any]]
        try:
            data = github_csv_to_dict(url)
        except Exception:
            data = []

        return data
