from .object import T_team
from .._element.source import DataSourceModel
from .model import TeamModel
from .._element.repository import RepositoryWithID
from typing import Generic
from abc import ABC


class BaseTeamRepository(RepositoryWithID[T_team, DataSourceModel[TeamModel]], ABC, Generic[T_team]): ...