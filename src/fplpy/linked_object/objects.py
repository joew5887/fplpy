from __future__ import annotations
from typing import Optional, Callable, overload, Any
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
from ..unlinked_object.chip.object import UnlinkedChip


from ..util.external.github import format_player_name


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
    
    @overload
    def player_summary_objects(self, source: Callable[[int], Repository[LinkedPlayerSummary, T_source]]) -> list[LinkedPlayerSummary]:
        ...

    @overload
    def player_summary_objects(self, source: Callable[[str,str], Repository[LinkedPlayerSummary, T_source]], season: str) -> list[LinkedPlayerSummary]:
        ...

    def player_summary_objects(self, source: Callable, season: Optional[str] = None) -> list[LinkedPlayerSummary]:
        repo: Repository[LinkedPlayerSummary, Any]

        try:
            repo = source(self.value.id)
        except TypeError:
            name = format_player_name(self.value.first_name, self.value.second_name, self.value.id)
            repo = source(season, name)  # adjust args as needed

        return repo.get_all()
    
    @overload
    def player_summary_df(self, source: Callable[[int], Repository[LinkedPlayerSummary, T_source]]) -> pd.DataFrame:
        ...

    @overload
    def player_summary_df(self, source: Callable[[str,str], Repository[LinkedPlayerSummary, T_source]], season: str) -> pd.DataFrame:
        ...
    
    def player_summary_df(self, source: Callable, season: Optional[str] = None) -> pd.DataFrame:
        if season is None:
            objs = self.player_summary_objects(source)
        else:
            objs = self.player_summary_objects(source, season)
        
        data = [asdict(obj.value) for obj in objs]
        df = pd.DataFrame(data)
        
        return df


class LinkedPosition(UnlinkedPosition):
    pass


class LinkedTeam(UnlinkedTeam):
    pass


class LinkedGameSettings(UnlinkedGameSettings):
    pass


class LinkedChip(UnlinkedChip):
    pass
