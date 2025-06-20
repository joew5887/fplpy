from .object import T_player
from .._element.source import DataSourceModel
from .model import PlayerModel
from .._element.repository import RepositoryWithID
from abc import ABC
from typing import Generic


class BasePlayerRepository(RepositoryWithID[T_player, DataSourceModel[PlayerModel]], ABC, Generic[T_player]): ...
