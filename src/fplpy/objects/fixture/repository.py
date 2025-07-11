from .._element.repository import RepositoryWithIDandCode
from .._element.source import DataSourceModel
from .model import FixtureModel
from .object import T_fixture
from typing import Generic
from abc import ABC


class FixtureRepository(RepositoryWithIDandCode[T_fixture, DataSourceModel[FixtureModel]], ABC, Generic[T_fixture]):
    pass
