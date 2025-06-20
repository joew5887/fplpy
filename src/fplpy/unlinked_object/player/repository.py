from .object import T_player
from .source import PlayerDataSource
from .._element.repository import BaseRepositoryWithID
from abc import ABC
from typing import Generic


class BasePlayerRepository(BaseRepositoryWithID[T_player, PlayerDataSource], ABC, Generic[T_player]): ...
