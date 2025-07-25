from enum import Enum
from typing import Any
from ..objects.summary import ObjTypes, RepoTypes, ObjNames
from ..util.external.github import format_player_name


# Data Sources
from ..objects.event.external.api import EventAPIDataSource
from ..objects.fixture.external.api import FixtureAPIDataSource
from ..objects.label.external.api import LabelAPIDataSource
from ..objects.player.external.api import PlayerAPIDataSource
from ..objects.position.external.api import PositionAPIDataSource
from ..objects.team.external.api import TeamAPIDataSource
from ..objects.game_settings.external.api import GameSettingsAPIDataSource
from ..objects.player_summary.external.api import PlayerSummaryAPIDataSource
from ..objects.chip.external.api import ChipAPIDataSource
from ..objects.player_history.external.api import PlayerHistoryAPIDataSource

from ..objects.fixture.external.github import FixtureGitHubDataSource
from ..objects.player.external.github import PlayerGitHubDataSource
from ..objects.team.external.github import TeamGitHubDataSource
from ..objects.player_summary.external.github import PlayerSummaryGitHubDataSource
from ..objects.player_history.external.github import PlayerHistoryGitHubDataSource

from ..objects.event.external.local import EventLocalDataSource


class Source(str, Enum):
    API = "api"
    GITHUB = "github"
    LOCAL = "local"


class IndividualRepositoryFactories:
    @staticmethod
    def chips(source: Source) -> RepoTypes.ChipRepo:
        if source == Source.API:
            return RepoTypes.ChipRepo(ObjTypes.Chip, ChipAPIDataSource())

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.CHIP, source))

    @staticmethod
    def players(source: Source, **kwargs) -> RepoTypes.PlayerRepo:
        if source == Source.API:
            return RepoTypes.PlayerRepo(ObjTypes.Player, PlayerAPIDataSource())
        elif source == Source.GITHUB:
            season = process_season_param(kwargs.get("season"))

            return RepoTypes.PlayerRepo(ObjTypes.Player, PlayerGitHubDataSource(season=season))

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.PLAYER, source))

    @staticmethod
    def events(source: Source, **kwargs) -> RepoTypes.EventRepo:
        if source == Source.API:
            return RepoTypes.EventRepo(ObjTypes.Event, EventAPIDataSource())
        elif source == Source.LOCAL:
            file_path = kwargs.get("file_path")
            if file_path is None:
                raise ValueError(f"Missing 'file_path' parameter")
            
            if not isinstance(file_path, str):
                raise TypeError(f"'file_path' must be a str")

            return RepoTypes.EventRepo(ObjTypes.Event, EventLocalDataSource(file_path=file_path))

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.EVENT, source))

    @staticmethod
    def player_summary(source: Source, player: ObjTypes.Player, **kwargs) -> RepoTypes.PlayerSummaryRepo:
        if source == Source.API:
            player_id = player.value.id

            return RepoTypes.PlayerSummaryRepo(ObjTypes.PlayerSummary, PlayerSummaryAPIDataSource(player_id=player_id))

        elif source == Source.GITHUB:
            season = process_season_param(kwargs.get("season"))
            
            name = format_player_name(
                player.value.first_name, player.value.second_name, player.value.id
            )

            return RepoTypes.PlayerSummaryRepo(
                ObjTypes.PlayerSummary,
                PlayerSummaryGitHubDataSource(
                    season=season,
                    player_name_formatted=name
                )
            )

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.PLAYER_SUMMARY, source))
    
    @staticmethod
    def player_history(source: Source, player: ObjTypes.Player, **kwargs) -> RepoTypes.PlayerHistoryRepo:
        if source == Source.API:
            player_id = player.value.id

            return RepoTypes.PlayerHistoryRepo(ObjTypes.PlayerHistory, PlayerHistoryAPIDataSource(player_id=player_id))

        elif source == Source.GITHUB:
            season = process_season_param(kwargs.get("season"))
            
            name = format_player_name(
                player.value.first_name, player.value.second_name, player.value.id
            )

            return RepoTypes.PlayerHistoryRepo(
                ObjTypes.PlayerHistory,
                PlayerHistoryGitHubDataSource(
                    season=season,
                    player_name_formatted=name
                )
            )

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.PLAYER_HISTORY, source))

    @staticmethod
    def fixtures(source: Source, **kwargs) -> RepoTypes.FixtureRepo:
        if source == Source.API:
            return RepoTypes.FixtureRepo(ObjTypes.Fixture, FixtureAPIDataSource())
        elif source == Source.GITHUB:
            season = process_season_param(kwargs.get("season"))

            return RepoTypes.FixtureRepo(ObjTypes.Fixture, FixtureGitHubDataSource(season=season))

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.FIXTURE, source))

    @staticmethod
    def teams(source: Source, **kwargs) -> RepoTypes.TeamRepo:
        if source == Source.API:
            return RepoTypes.TeamRepo(ObjTypes.Team, TeamAPIDataSource())
        elif source == Source.GITHUB:
            season = process_season_param(kwargs.get("season"))

            return RepoTypes.TeamRepo(ObjTypes.Team, TeamGitHubDataSource(season=season))

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.TEAM, source))

    @staticmethod
    def positions(source: Source) -> RepoTypes.PositionRepo:
        if source == Source.API:
            return RepoTypes.PositionRepo(ObjTypes.Position, PositionAPIDataSource())

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.POSITION, source))

    @staticmethod
    def game_settings(source: Source) -> RepoTypes.GameSettingsRepo:
        if source == Source.API:
            return RepoTypes.GameSettingsRepo(ObjTypes.GameSettings, GameSettingsAPIDataSource())

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.GAME_SETTINGS, source))

    @staticmethod
    def labels(source: Source) -> RepoTypes.LabelRepo:
        if source == Source.API:
            return RepoTypes.LabelRepo(ObjTypes.Label, LabelAPIDataSource())

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.LABEL, source))


def _not_implemented_error_msg(repo_type: ObjNames, source: Source) -> str:
    return f"Unsupported repository for {repo_type} repository with source {source}."


def process_season_param(season: Any) -> str:
    if season is None:
        raise ValueError(f"Missing 'season' parameter")
            
    if not isinstance(season, str):
        raise TypeError(f"'season' must be a str")
        
    return season
