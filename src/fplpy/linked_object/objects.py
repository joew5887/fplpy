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


class LinkedEvent(UnlinkedEvent):
    pass


class LinkedFixture(UnlinkedFixture):
    def team_h(self, source: BaseTeamRepository[LinkedTeam]) -> LinkedTeam:
        res = source.get_filtered(lambda x: x.value.id == self.value.team_h)
        
        return LinkedTeam(res[0].value)
    
    def team_a(self, source: BaseTeamRepository[LinkedTeam]) -> LinkedTeam:
        res = source.get_filtered(lambda x: x.value.id == self.value.team_a)
        
        return LinkedTeam(res[0].value)
    
    def event(self, source: BaseEventRepository[LinkedEvent]) -> Optional[LinkedEvent]:
        res = source.get_by_id(self.value.event)
        
        if res is not None:
            return LinkedEvent(res.value)
        
        return None


class LinkedLabel(UnlinkedLabel):
    pass


class LinkedPlayer(UnlinkedPlayer):
    def position(self, source: BasePositionRepository[LinkedPosition]) -> Optional[LinkedPosition]:
        res = source.get_by_id(self.value.element_type)
        
        if res is not None:
            return LinkedPosition(res.value)
        
        return None
    
    def team(self, source: BaseTeamRepository[LinkedTeam]) -> LinkedTeam:
        res = source.get_filtered(lambda x: x.value.id == self.value.team)
        
        return LinkedTeam(res[0].value)

class LinkedPosition(UnlinkedPosition):
    pass


class LinkedTeam(UnlinkedTeam):
    pass
