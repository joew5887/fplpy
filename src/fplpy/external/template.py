from abc import ABC, abstractmethod


class ExternalFPLData(ABC):
    @abstractmethod
    def get_teams(self) -> list[dict]:
        return None
    
    @abstractmethod
    def get_fixtures(self) -> list[dict]:
        return None
    
    @abstractmethod
    def get_players(self) -> list[dict]:
        return None
