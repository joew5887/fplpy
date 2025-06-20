from .object import T_position
from .source import PositionDataSource
from .._element.repository import BaseRepositoryWithID
from typing import Generic
from abc import ABC


class BasePositionRepository(BaseRepositoryWithID[T_position, PositionDataSource], ABC, Generic[T_position]):
    def get_short_to_full_name_dict(self) -> dict[str, T_position]:
        """Get all positions, with the keys as the `singular_name_short`.

        Returns
        -------
        dict[str, Position]
            ```{"GKP": Goalkeeper, ..., "FWD": Forward}```
        """
        positions = self.get_all()

        return {position.value.singular_name_short: position for position in positions}
