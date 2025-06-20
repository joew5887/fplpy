from __future__ import annotations
from typing import Optional

from ..unlinked_object.event.object import Event as UnlinkedEvent
from ..unlinked_object.fixture.object import Fixture as UnlinkedFixture
from ..unlinked_object.label.object import Label as UnlinkedLabel
from ..unlinked_object.player.object import Player as UnlinkedPlayer
from ..unlinked_object.position.object import Position as UnlinkedPosition
from ..unlinked_object.team.object import Team as UnlinkedTeam

from ..unlinked_object.team.repository import BaseTeamRepository
from ..unlinked_object.event.repository import BaseEventRepository
from ..unlinked_object.position.repository import BasePositionRepository

from .template import LinkedFixtureTemplate, LinkedEventTemplate, \
    LinkedPositionTemplate, LinkedTeamTemplate, LinkedLabelTemplate, \
    LinkedPlayerTemplate


class LinkedEvent(UnlinkedEvent, LinkedEventTemplate): ...
class LinkedFixture(UnlinkedFixture, LinkedFixtureTemplate):
    def team_h(self, source: BaseTeamRepository[LinkedTeamTemplate]) -> LinkedTeam:
        res = source.get_filtered(lambda x: x.value.id == self.value.team_h)
        
        return LinkedTeam(res[0].value)
    
    def team_a(self, source: BaseTeamRepository[LinkedTeamTemplate]) -> LinkedTeam:
        res = source.get_filtered(lambda x: x.value.id == self.value.team_a)
        
        return LinkedTeam(res[0].value)
    
    def event(self, source: BaseEventRepository[LinkedEventTemplate]) -> Optional[LinkedEvent]:
        res = source.get_by_id(self.value.event)
        
        if res is not None:
            return LinkedEvent(res.value)
        
        return None
    
class LinkedLabel(UnlinkedLabel, LinkedLabelTemplate): ...
class LinkedPlayer(UnlinkedPlayer, LinkedPlayerTemplate):
    def position(self, source: BasePositionRepository[LinkedPositionTemplate]) -> Optional[LinkedPosition]:
        res = source.get_by_id(self.value.element_type)
        
        if res is not None:
            return LinkedPosition(res.value)
        
        return None
    
    def team(self, source: BaseTeamRepository[LinkedTeamTemplate]) -> LinkedTeam:
        res = source.get_filtered(lambda x: x.value.id == self.value.team)
        
        return LinkedTeam(res[0].value)

class LinkedPosition(UnlinkedPosition, LinkedPositionTemplate): ...
class LinkedTeam(UnlinkedTeam, LinkedTeamTemplate):
    def foo(self) -> str:
        return "testing"
