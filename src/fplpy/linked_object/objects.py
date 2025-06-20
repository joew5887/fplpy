from __future__ import annotations
from typing import Optional

from ..unlinked_object._element.repository import RepositoryWithID
from ..unlinked_object._element.source import T_source

from ..unlinked_object.event.object import UnlinkedEvent
from ..unlinked_object.fixture.object import UnlinkedFixture
from ..unlinked_object.label.object import UnlinkedLabel
from ..unlinked_object.player.object import UnlinkedPlayer
from ..unlinked_object.position.object import UnlinkedPosition
from ..unlinked_object.team.object import UnlinkedTeam
from ..unlinked_object.game_settings.object import UnlinkedGameSettings


class LinkedEvent(UnlinkedEvent):
    pass


class LinkedFixture(UnlinkedFixture):
    def team_h(self, source: RepositoryWithID[LinkedTeam, T_source]) -> LinkedTeam:
        res = source.get_filtered(lambda x: x.value.id == self.value.team_h)
        
        return LinkedTeam(res[0].value)
    
    def team_a(self, source: RepositoryWithID[LinkedTeam, T_source]) -> LinkedTeam:
        res = source.get_filtered(lambda x: x.value.id == self.value.team_a)
        
        return LinkedTeam(res[0].value)
    
    def event(self, source: RepositoryWithID[LinkedEvent, T_source]) -> Optional[LinkedEvent]:
        res = source.get_by_id(self.value.event)
        
        if res is not None:
            return LinkedEvent(res.value)
        
        return None


class LinkedLabel(UnlinkedLabel):
    pass


class LinkedPlayer(UnlinkedPlayer):
    def position(self, source: RepositoryWithID[LinkedPosition, T_source]) -> Optional[LinkedPosition]:
        res = source.get_by_id(self.value.element_type)
        
        if res is not None:
            return LinkedPosition(res.value)
        
        return None
    
    def team(self, source: RepositoryWithID[LinkedTeam, T_source]) -> LinkedTeam:
        res = source.get_filtered(lambda x: x.value.id == self.value.team)
        
        return LinkedTeam(res[0].value)

class LinkedPosition(UnlinkedPosition):
    pass


class LinkedTeam(UnlinkedTeam):
    pass


class LinkedGameSettings(UnlinkedGameSettings):
    pass
