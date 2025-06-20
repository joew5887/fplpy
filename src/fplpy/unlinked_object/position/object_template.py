from __future__ import annotations
from .._element.element import ElementWithID
from .model import PositionModel
from abc import ABC


class PositionTemplate(ElementWithID[PositionModel], ABC):
    pass
