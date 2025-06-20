from __future__ import annotations
from .._element.element import ElementWithID
from .model import FixtureModel
from abc import ABC


class FixtureTemplate(ElementWithID[FixtureModel], ABC): ...