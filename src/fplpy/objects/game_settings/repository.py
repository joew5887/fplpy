from .._element.repository import Repository
from .._element.source import DataSourceModel
from .model import GameSettingsModel
from .object import T_GameSettings
from typing import Generic
from abc import ABC


class GameSettingsRepository(Repository[T_GameSettings, DataSourceModel[GameSettingsModel]], ABC, Generic[T_GameSettings]):
    pass
