from .._element.repository import Repository
from .._element.source import DataSourceModel
from .model import PlayerSummaryModel
from .object import T_player_summary
from typing import Generic
from abc import ABC
import pandas as pd
from dataclasses import asdict


class PlayerSummaryRepository(Repository[T_player_summary, DataSourceModel[PlayerSummaryModel]], ABC, Generic[T_player_summary]):
    def as_df(self) -> pd.DataFrame:
        data = [asdict(obj.value) for obj in self.get_all()]
        df = pd.DataFrame(data)
        
        return df
