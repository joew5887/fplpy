from __future__ import annotations
from .._element.element import ElementWithID
from .model import PlayerModel
from abc import ABC


class PlayerTemplate(ElementWithID[PlayerModel], ABC): ...