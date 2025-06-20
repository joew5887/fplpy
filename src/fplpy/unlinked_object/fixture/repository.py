from .object import T_fixture
from .._element.source import DataSourceModel
from .model import FixtureModel
from .._element.repository import RepositoryWithID
from typing import Generic
from abc import ABC


class BaseFixtureRepository(RepositoryWithID[T_fixture, DataSourceModel[FixtureModel]], ABC, Generic[T_fixture]): ...
