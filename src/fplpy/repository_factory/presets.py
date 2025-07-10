from .general import IndividualRepositoryFactories, Source
from .template import RepositoryFactoryTemplate
from ..objects.summary import RepoTypes, ObjTypes


class APIRepositoryFactory(RepositoryFactoryTemplate):
    def chips(self) -> RepoTypes.Chip:
        return IndividualRepositoryFactories.chips(Source.API)
    
    def players(self) -> RepoTypes.Player:
        return IndividualRepositoryFactories.players(Source.API)
    
    def events(self) -> RepoTypes.Event:
        return IndividualRepositoryFactories.events(Source.API)
    
    def player_summary(self, player: ObjTypes.Player) -> RepoTypes.PlayerSummary:
        return IndividualRepositoryFactories.player_summary(Source.API, player)
    
    def fixtures(self) -> RepoTypes.Fixture:
        return IndividualRepositoryFactories.fixtures(Source.API)
    
    def teams(self) -> RepoTypes.Team:
        return IndividualRepositoryFactories.teams(Source.API)
    
    def positions(self) -> RepoTypes.Position:
        return IndividualRepositoryFactories.positions(Source.API)
    
    def game_settings(self) -> RepoTypes.GameSettings:
        return IndividualRepositoryFactories.game_settings(Source.API)
    
    def labels(self) -> RepoTypes.Label:
        return IndividualRepositoryFactories.labels(Source.API)
