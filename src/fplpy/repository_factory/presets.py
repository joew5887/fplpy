from .general import IndividualRepositoryFactories, Source
from .template import RepositoryFactoryTemplate
from ..objects.summary import RepoTypes, ObjTypes
import os


class APIRepositoryFactory(RepositoryFactoryTemplate):
    def chips(self) -> RepoTypes.ChipRepo:
        return IndividualRepositoryFactories.chips(Source.API)
    
    def players(self) -> RepoTypes.PlayerRepo:
        return IndividualRepositoryFactories.players(Source.API)
    
    def events(self) -> RepoTypes.EventRepo:
        return IndividualRepositoryFactories.events(Source.API)
    
    def player_summary(self, player: ObjTypes.Player) -> RepoTypes.PlayerSummaryRepo:
        return IndividualRepositoryFactories.player_summary(Source.API, player)
    
    def player_history(self, player: ObjTypes.Player) -> RepoTypes.PlayerHistoryRepo:
        return IndividualRepositoryFactories.player_history(Source.API, player)
    
    def fixtures(self) -> RepoTypes.FixtureRepo:
        return IndividualRepositoryFactories.fixtures(Source.API)
    
    def teams(self) -> RepoTypes.TeamRepo:
        return IndividualRepositoryFactories.teams(Source.API)
    
    def positions(self) -> RepoTypes.PositionRepo:
        return IndividualRepositoryFactories.positions(Source.API)
    
    def game_settings(self) -> RepoTypes.GameSettingsRepo:
        return IndividualRepositoryFactories.game_settings(Source.API)
    
    def labels(self) -> RepoTypes.LabelRepo:
        return IndividualRepositoryFactories.labels(Source.API)
    
    
class GitHubRepositoryFactory(RepositoryFactoryTemplate):
    def __init__(self, season: str) -> None:
        self.__season = season

    def chips(self) -> RepoTypes.ChipRepo:
        return IndividualRepositoryFactories.chips(Source.API)
    
    def players(self) -> RepoTypes.PlayerRepo:
        return IndividualRepositoryFactories.players(Source.GITHUB, season=self.__season)
    
    def events(self) -> RepoTypes.EventRepo:
        return IndividualRepositoryFactories.events(Source.API)
    
    def player_summary(self, player: ObjTypes.Player) -> RepoTypes.PlayerSummaryRepo:
        return IndividualRepositoryFactories.player_summary(Source.GITHUB, player, season=self.__season)
    
    def player_history(self, player: ObjTypes.Player) -> RepoTypes.PlayerHistoryRepo:
        return IndividualRepositoryFactories.player_history(Source.GITHUB, player, season=self.__season)
    
    def fixtures(self) -> RepoTypes.FixtureRepo:
        return IndividualRepositoryFactories.fixtures(Source.GITHUB, season=self.__season)
    
    def teams(self) -> RepoTypes.TeamRepo:
        return IndividualRepositoryFactories.teams(Source.GITHUB, season=self.__season)
    
    def positions(self) -> RepoTypes.PositionRepo:
        return IndividualRepositoryFactories.positions(Source.API)
    
    def game_settings(self) -> RepoTypes.GameSettingsRepo:
        return IndividualRepositoryFactories.game_settings(Source.API)
    
    def labels(self) -> RepoTypes.LabelRepo:
        return IndividualRepositoryFactories.labels(Source.API)
    

class RepositoryFactory202425(GitHubRepositoryFactory):
    def __init__(self, event_file_path: str) -> None:
        super().__init__("2024-25")
        
        self.__event_file_path = event_file_path
        
    def events(self) -> RepoTypes.EventRepo:
        return IndividualRepositoryFactories.events(Source.LOCAL, file_path=self.__event_file_path)
