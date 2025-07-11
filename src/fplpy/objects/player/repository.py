from .._element.repository import RepositoryWithIDandCode
from .._element.source import DataSourceModel
from .model import PlayerModel
from .object import T_player
from typing import Generic
from abc import ABC


class PlayerRepository(RepositoryWithIDandCode[T_player, DataSourceModel[PlayerModel]], ABC, Generic[T_player]):
    pass
