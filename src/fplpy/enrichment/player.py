from .template import BaseEnricher
from ..objects.summary import ObjTypes
from typing import TypedDict, Optional


class PlayerEnrichmentOutput(TypedDict):
    team: Optional[ObjTypes.Team]
    position: Optional[ObjTypes.Position]


class PlayerEnricher(BaseEnricher[ObjTypes.Player, PlayerEnrichmentOutput]):
    def enrich(self, obj: ObjTypes.Player) -> PlayerEnrichmentOutput:
        team_repo = self._repo_factory.teams()
        team = team_repo.get_by_code(obj.value.team_code)
        
        position_repo = self._repo_factory.positions()
        position = position_repo.get_by_id(obj.value.element_type)
        
        return {
            "team": team,
            "position": position
        }
