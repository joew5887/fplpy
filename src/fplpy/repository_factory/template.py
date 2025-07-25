from ..objects.summary import RepoTypes, ObjTypes
from abc import ABC, abstractmethod


class RepositoryFactoryTemplate(ABC):
    @abstractmethod
    def chips(self) -> RepoTypes.ChipRepo:
        ...
    
    @abstractmethod
    def players(self) -> RepoTypes.PlayerRepo:
        ...
    
    @abstractmethod
    def events(self) -> RepoTypes.EventRepo:
        ...
    
    @abstractmethod
    def player_summary(self, player: ObjTypes.Player) -> RepoTypes.PlayerSummaryRepo:
        ...
        
    @abstractmethod
    def player_history(self, player: ObjTypes.Player) -> RepoTypes.PlayerHistoryRepo:
        ...
    
    @abstractmethod
    def fixtures(self) -> RepoTypes.FixtureRepo:
        ...
    
    @abstractmethod
    def teams(self) -> RepoTypes.TeamRepo:
        ...
    
    @abstractmethod
    def positions(self) -> RepoTypes.PositionRepo:
        ...
    
    @abstractmethod
    def game_settings(self) -> RepoTypes.GameSettingsRepo:
        ...
    
    @abstractmethod
    def labels(self) -> RepoTypes.LabelRepo:
        ...
