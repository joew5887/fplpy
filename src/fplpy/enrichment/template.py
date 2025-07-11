from typing import Generic, TypeVar
from abc import ABC, abstractmethod
from ..repository_factory.template import RepositoryFactoryTemplate

T_input = TypeVar("T_input")  # Input object type
T_output = TypeVar("T_output")  # Enriched result type

class Enrichable(ABC):
    id: int

class BaseEnricher(Generic[T_input, T_output]):
    def __init__(self, repo_factory: RepositoryFactoryTemplate) -> None:
        self._repo_factory = repo_factory
    
    @abstractmethod
    def enrich(self, obj: T_input) -> T_output:
        ...
