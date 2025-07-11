from .._element.repository import RepositoryWithIDandCode
from .._element.source import DataSourceModel
from .model import TeamModel
from .object import T_team
from typing import Generic
from abc import ABC


class TeamRepository(RepositoryWithIDandCode[T_team, DataSourceModel[TeamModel]], ABC, Generic[T_team]):
    pass
