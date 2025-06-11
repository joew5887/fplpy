from abc import ABC, abstractmethod
from typing import Any


class ExternalFPLData(ABC):
    @abstractmethod
    def get_teams(self) -> list[dict[str, Any]]: ...

    @abstractmethod
    def get_fixtures(self) -> list[dict[str, Any]]: ...

    @abstractmethod
    def get_players(self) -> list[dict[str, Any]]: ...
