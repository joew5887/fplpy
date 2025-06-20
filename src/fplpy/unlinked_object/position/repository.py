from .object import T_position
from .._element.source import DataSourceModel
from .model import PositionModel
from .._element.repository import RepositoryWithID
from typing import Generic
from abc import ABC


class BasePositionRepository(RepositoryWithID[T_position, DataSourceModel[PositionModel]], ABC, Generic[T_position]):
    def get_short_to_full_name_dict(self) -> dict[str, T_position]:
        """Get all positions, with the keys as the `singular_name_short`.

        Returns
        -------
        dict[str, Position]
            ```{"GKP": Goalkeeper, ..., "FWD": Forward}```
        """
        positions = self.get_all()

        return {position.value.singular_name_short: position for position in positions}
