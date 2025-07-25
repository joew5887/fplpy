from .template import BaseEnricher
from ..objects.summary import ObjTypes
from .fixture import FixtureEnricher
from typing import TypedDict, Optional


class PlayerSummaryEnrichmentOutput(TypedDict):
    event: ObjTypes.Event
    fixture: ObjTypes.Fixture


class PlayerSummaryEnricher(BaseEnricher[ObjTypes.PlayerSummary, PlayerSummaryEnrichmentOutput]):
    def enrich(self, obj: ObjTypes.PlayerSummary) -> PlayerSummaryEnrichmentOutput:
        fixture_repo = self._repo_factory.fixtures()
        
        fixture = fixture_repo.get_by_id(obj.value.fixture)
        if fixture is None:
            raise Exception("Enriching player_summary's fixture returned None")
        
        fixture_enrich_engine = FixtureEnricher(self._repo_factory)
        fixture_enriched = fixture_enrich_engine.enrich(fixture)
        event = fixture_enriched["event"]
        if event is None:
            raise Exception("Enriching player_summary's event returned None")
        
        return {
            "event": event,
            "fixture": fixture
        }
