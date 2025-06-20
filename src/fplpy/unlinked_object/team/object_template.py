from __future__ import annotations
from .._element.element import ElementWithID
from .model import TeamModel
from abc import ABC


class TeamTemplate(ElementWithID[TeamModel], ABC): ...