from ..objects.summary import RepoTypes, ObjTypes
from abc import ABC, abstractmethod


class RepositoryFactoryTemplate(ABC):
    @abstractmethod
    def chips(self) -> RepoTypes.Chip:
        ...
    
    @abstractmethod
    def players(self) -> RepoTypes.Player:
        ...
    
    @abstractmethod
    def events(self) -> RepoTypes.Event:
        ...
    
    @abstractmethod
    def player_summary(self, player: ObjTypes.Player) -> RepoTypes.PlayerSummary:
        ...
    
    @abstractmethod
    def fixtures(self) -> RepoTypes.Fixture:
        ...
    
    @abstractmethod
    def teams(self) -> RepoTypes.Team:
        ...
    
    @abstractmethod
    def positions(self) -> RepoTypes.Position:
        ...
    
    @abstractmethod
    def game_settings(self) -> RepoTypes.GameSettings:
        ...
    
    @abstractmethod
    def labels(self) -> RepoTypes.Label:
        ...
