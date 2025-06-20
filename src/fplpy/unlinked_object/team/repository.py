from .object import T_team
from .source import TeamDataSource
from .._element.repository import BaseRepositoryWithID
from typing import Generic
from abc import ABC


class BaseTeamRepository(BaseRepositoryWithID[T_team, TeamDataSource], ABC, Generic[T_team]): ...
