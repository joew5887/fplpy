from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

from ..unlinked_object.event.object_template import EventTemplate as UnlinkedEventTemplate
from ..unlinked_object.fixture.object_template import FixtureTemplate as UnlinkedFixtureTemplate
from ..unlinked_object.label.object_template import LabelTemplate as UnlinkedLabelTemplate
from ..unlinked_object.player.object_template import PlayerTemplate as UnlinkedPlayerTemplate
from ..unlinked_object.position.object_template import PositionTemplate as UnlinkedPositionTemplate
from ..unlinked_object.team.object_template import TeamTemplate as UnlinkedTeamTemplate

from ..unlinked_object.team.repository import BaseTeamRepository
from ..unlinked_object.event.repository import BaseEventRepository
from ..unlinked_object.position.repository import BasePositionRepository

class LinkedEventTemplate(UnlinkedEventTemplate, ABC): ...
class LinkedFixtureTemplate(UnlinkedFixtureTemplate, ABC):
    @abstractmethod
    def team_h(self, source: BaseTeamRepository[LinkedTeamTemplate]) -> LinkedTeamTemplate: ...

    @abstractmethod
    def team_a(self, source: BaseTeamRepository[LinkedTeamTemplate]) -> LinkedTeamTemplate: ...

    @abstractmethod
    def event(self, source: BaseEventRepository[LinkedEventTemplate]) -> Optional[LinkedEventTemplate]: ...

class LinkedLabelTemplate(UnlinkedLabelTemplate, ABC): ...
class LinkedPlayerTemplate(UnlinkedPlayerTemplate, ABC):
    @abstractmethod
    def position(self, source: BasePositionRepository["LinkedPositionTemplate"]) -> Optional[LinkedPositionTemplate]: ...
    
    @abstractmethod
    def team(self, source: BaseTeamRepository[LinkedTeamTemplate]) -> LinkedTeamTemplate: ...

class LinkedPositionTemplate(UnlinkedPositionTemplate, ABC): ...

class LinkedTeamTemplate(UnlinkedTeamTemplate, ABC):
    @abstractmethod
    def foo(self) -> str: ...