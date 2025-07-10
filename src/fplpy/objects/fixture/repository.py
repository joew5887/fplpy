from .._element.repository import Repository
from .._element.source import DataSourceModel
from .model import FixtureModel
from .object import T_fixture
from typing import Generic
from abc import ABC


class FixtureRepository(Repository[T_fixture, DataSourceModel[FixtureModel]], ABC, Generic[T_fixture]):
    pass
