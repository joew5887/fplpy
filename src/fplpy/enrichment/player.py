from .template import BaseEnricher
from ..objects.summary import ObjTypes, RepoTypes
from ..repository_factory.template import RepositoryFactoryTemplate
from typing import TypedDict, Optional, TypeVar, Any
from .player_summary import PlayerSummaryEnricher


T = TypeVar("T")


class PlayerEnrichmentOutput(TypedDict):
    team: ObjTypes.Team
    position: ObjTypes.Position


class PlayerEnricher(BaseEnricher[ObjTypes.Player, PlayerEnrichmentOutput]):
    def enrich(self, obj: ObjTypes.Player) -> PlayerEnrichmentOutput:
        team_repo = self._repo_factory.teams()
        team = team_repo.get_by_code(obj.value.team_code)
        
        if team is None:
            raise Exception("Enriching player's team returned None")
        
        position_repo = self._repo_factory.positions()
        position = position_repo.get_by_id(obj.value.element_type)
        
        if position is None:
            raise Exception("Enriching player's position returned None")
        
        return {
            "team": team,
            "position": position
        }
        
        
class PlayerCostTracker:
    # Assuming the cost in each PlayerSummary record is the cost at the DEADLINE TIME of the fixture's gameweek
    # Assuming the GW1 record in PlayerSummary == start_cost
    __cost_at_event_filled: dict[ObjTypes.Event, int]
    __player: ObjTypes.Player

    def __init__(self, player: ObjTypes.Player, cost_at_event_filled: dict[ObjTypes.Event, int]) -> None:
        self.__player = player
        self.__cost_at_event_filled = cost_at_event_filled
        
    @property
    def player(self) -> ObjTypes.Player:
        return self.__player

    def cost_at_event_begin(self, event: ObjTypes.Event, default_cost: int = 0) -> int:
        cost = self.__cost_at_event_filled[event]
        
        if cost == 0:
            return default_cost
        
        return cost
    
    def serialise(self) -> dict[str, Any]:
        return {
            "player_code": self.__player.code,  # or another unique identifier
            "event_cost_map": {
                event.id: cost
                for event, cost in self.__cost_at_event_filled.items()
            }
        }
        
    @classmethod
    def deserialise(cls, data: dict[str, Any], repo_factory: RepositoryFactoryTemplate) -> "PlayerCostTracker":
        players_repo = repo_factory.players()
        player = players_repo.get_by_code(data["player_code"])  # assume this exists
        if player is None:
            raise ValueError("Player code not found in repo.")
        
        events_repo = repo_factory.events()

        # Rebuild the event objects
        event_map = {}
        for event in events_repo.get_all():
            if str(event.id) in data["event_cost_map"]:
                event_map[event] = data["event_cost_map"][str(event.id)]

        cost_at_event_filled = fill_event_dict(event_map, events_repo, 0)

        return cls(player, cost_at_event_filled)
    
    @classmethod
    def from_player(cls, player: ObjTypes.Player, repo_factory: RepositoryFactoryTemplate) -> "PlayerCostTracker":
        cost_at_event_unfilled: dict[ObjTypes.Event, int] = get_cost_at_event_unfilled(player, repo_factory)
        cost_at_event_filled = fill_event_dict(cost_at_event_unfilled, repo_factory.events(), 0)
        
        return cls(player, cost_at_event_filled)
    
    
def get_cost_at_event_unfilled(player: ObjTypes.Player, repo_factory: RepositoryFactoryTemplate) -> dict[ObjTypes.Event, int]:
    cost_at_event_unfilled: dict[ObjTypes.Event, int] = {}
    player_summary_repo = repo_factory.player_summary(player)
    enrich_engine = PlayerSummaryEnricher(repo_factory)

    for player_summary in player_summary_repo.get_all():
        cost = player_summary.value.value
        player_summary_enriched = enrich_engine.enrich(player_summary)
        event = player_summary_enriched["event"]
            
        cost_at_event_unfilled[event] = cost
        
    return cost_at_event_unfilled


def fill_event_dict(event_dict_unfilled: dict[ObjTypes.Event, T], events_repo: RepoTypes.EventRepo, default_value: T) -> dict[ObjTypes.Event, T]:
    event_dict_filled = {}
    last_value: Optional[T] = None
    events = events_repo.get_all()

    for event in events:
        if event in event_dict_unfilled:
            value = event_dict_unfilled[event]
            last_value = value
            event_dict_filled[event] = value
        else:
            event_dict_filled[event] = last_value if last_value is not None else default_value
            
    return event_dict_filled
