from __future__ import annotations
from .._element.element import Element
from .model import LabelModel
from abc import ABC


class LabelTemplate(Element[LabelModel], ABC): ...
