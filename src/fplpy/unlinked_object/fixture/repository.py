from .object import T_fixture
from .source import FixtureDataSource
from .._element.repository import BaseRepositoryWithID
from typing import Generic
from abc import ABC


class BaseFixtureRepository(BaseRepositoryWithID[T_fixture, FixtureDataSource], ABC, Generic[T_fixture]): ...
