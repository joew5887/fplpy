from .template import BaseEnricher
from ..objects.summary import ObjTypes
from typing import TypedDict, Optional


class FixtureEnrichmentOutput(TypedDict):
    event: Optional[ObjTypes.Event]
    team_h: Optional[ObjTypes.Team]
    team_a: Optional[ObjTypes.Team]


class FixtureEnricher(BaseEnricher[ObjTypes.Fixture, FixtureEnrichmentOutput]):
    def enrich(self, obj: ObjTypes.Fixture) -> FixtureEnrichmentOutput:
        team_repo = self._repo_factory.teams()
        team_h = team_repo.get_by_id(obj.value.team_h)
        team_a = team_repo.get_by_id(obj.value.team_a)
        
        event_repo = self._repo_factory.events()
        event = event_repo.get_by_id(obj.value.event)
        
        return {
            "event": event,
            "team_h": team_h,
            "team_a": team_a
        }
