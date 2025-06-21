from __future__ import annotations
from typing import Optional, Callable
import pandas as pd
from dataclasses import asdict

from ..unlinked_object._element.repository import RepositoryWithID, Repository
from ..unlinked_object._element.source import T_source

from ..unlinked_object.event.object import UnlinkedEvent
from ..unlinked_object.fixture.object import UnlinkedFixture
from ..unlinked_object.label.object import UnlinkedLabel
from ..unlinked_object.player.object import UnlinkedPlayer
from ..unlinked_object.position.object import UnlinkedPosition
from ..unlinked_object.team.object import UnlinkedTeam
from ..unlinked_object.game_settings.object import UnlinkedGameSettings
from ..unlinked_object.player_summary.object import UnlinkedPlayerSummary


class LinkedPlayerSummary(UnlinkedPlayerSummary):
    pass


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
    
    def player_summary_objects(self, source: Callable[[int], Repository[LinkedPlayerSummary, T_source]]) -> list[LinkedPlayerSummary]:
        repo = source(self.value.id)
        
        return repo.get_all()
    
    def player_summary_df(self, source: Callable[[int], Repository[LinkedPlayerSummary, T_source]]) -> pd.DataFrame:
        objs = self.player_summary_objects(source)
        
        data = [asdict(obj.value) for obj in objs]
        df = pd.DataFrame(data)
        
        return df


class LinkedPosition(UnlinkedPosition):
    pass


class LinkedTeam(UnlinkedTeam):
    pass


class LinkedGameSettings(UnlinkedGameSettings):
    pass
