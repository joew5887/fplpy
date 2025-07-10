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

from ..objects.fixture.external.github import FixtureGitHubDataSource
from ..objects.player.external.github import PlayerGitHubDataSource
from ..objects.team.external.github import TeamGitHubDataSource
from ..objects.player_summary.external.github import PlayerSummaryGitHubDataSource

from ..objects.event.external.local import EventLocalDataSource


class Source(str, Enum):
    API = "api"
    GITHUB = "github"
    LOCAL = "local"


class IndividualRepositoryFactories:
    @staticmethod
    def chips(source: Source) -> RepoTypes.Chip:
        if source == Source.API:
            return RepoTypes.Chip(ObjTypes.Chip, ChipAPIDataSource())

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.CHIP, source))

    @staticmethod
    def players(source: Source, **kwargs) -> RepoTypes.Player:
        if source == Source.API:
            return RepoTypes.Player(ObjTypes.Player, PlayerAPIDataSource())
        elif source == Source.GITHUB:
            season = process_season_param(kwargs.get("season"))

            return RepoTypes.Player(ObjTypes.Player, PlayerGitHubDataSource(season=season))

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.PLAYER, source))

    @staticmethod
    def events(source: Source, **kwargs) -> RepoTypes.Event:
        if source == Source.API:
            return RepoTypes.Event(ObjTypes.Event, EventAPIDataSource())
        elif source == Source.LOCAL:
            file_path = kwargs.get("file_path")
            if file_path is None:
                raise ValueError(f"Missing 'file_path' parameter")
            
            if not isinstance(file_path, str):
                raise TypeError(f"'file_path' must be a str")

            return RepoTypes.Event(ObjTypes.Event, EventLocalDataSource(file_path=file_path))

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.EVENT, source))

    @staticmethod
    def player_summary(source: Source, player: ObjTypes.Player, **kwargs) -> RepoTypes.PlayerSummary:
        if source == Source.API:
            player_id = player.value.id

            return RepoTypes.PlayerSummary(ObjTypes.PlayerSummary, PlayerSummaryAPIDataSource(player_id=player_id))

        elif source == Source.GITHUB:
            season = process_season_param(kwargs.get("season"))
            
            name = format_player_name(
                player.value.first_name, player.value.second_name, player.value.id
            )

            return RepoTypes.PlayerSummary(
                ObjTypes.PlayerSummary,
                PlayerSummaryGitHubDataSource(
                    season=season,
                    player_name_formatted=name
                )
            )

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.PLAYER_SUMMARY, source))

    @staticmethod
    def fixtures(source: Source, **kwargs) -> RepoTypes.Fixture:
        if source == Source.API:
            return RepoTypes.Fixture(ObjTypes.Fixture, FixtureAPIDataSource())
        elif source == Source.GITHUB:
            season = process_season_param(kwargs.get("season"))

            return RepoTypes.Fixture(ObjTypes.Fixture, FixtureGitHubDataSource(season=season))

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.FIXTURE, source))

    @staticmethod
    def teams(source: Source, **kwargs) -> RepoTypes.Team:
        if source == Source.API:
            return RepoTypes.Team(ObjTypes.Team, TeamAPIDataSource())
        elif source == Source.GITHUB:
            season = process_season_param(kwargs.get("season"))

            return RepoTypes.Team(ObjTypes.Team, TeamGitHubDataSource(season=season))

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.TEAM, source))

    @staticmethod
    def positions(source: Source) -> RepoTypes.Position:
        if source == Source.API:
            return RepoTypes.Position(ObjTypes.Position, PositionAPIDataSource())

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.POSITION, source))

    @staticmethod
    def game_settings(source: Source) -> RepoTypes.GameSettings:
        if source == Source.API:
            return RepoTypes.GameSettings(ObjTypes.GameSettings, GameSettingsAPIDataSource())

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.GAME_SETTINGS, source))

    @staticmethod
    def labels(source: Source) -> RepoTypes.Label:
        if source == Source.API:
            return RepoTypes.Label(ObjTypes.Label, LabelAPIDataSource())

        raise NotImplementedError(_not_implemented_error_msg(ObjNames.LABEL, source))


def _not_implemented_error_msg(repo_type: ObjNames, source: Source) -> str:
    return f"Unsupported repository for {repo_type} repository with source {source}."


def process_season_param(season: Any) -> str:
    if season is None:
        raise ValueError(f"Missing 'season' parameter")
            
    if not isinstance(season, str):
        raise TypeError(f"'season' must be a str")
        
    return season
