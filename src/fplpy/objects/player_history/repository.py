from .._element.repository import Repository
from .._element.source import DataSourceModel
from .model import PlayerHistoryModel
from .object import T_player_history
from typing import Generic
from abc import ABC
import pandas as pd
from dataclasses import asdict


class PlayerHistoryRepository(Repository[T_player_history, DataSourceModel[PlayerHistoryModel]], ABC, Generic[T_player_history]):
    def as_df(self) -> pd.DataFrame:
        data = [asdict(obj.value) for obj in self.get_all()]
        df = pd.DataFrame(data)
        
        return df