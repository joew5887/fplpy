from __future__ import annotations
from .element_template import ElementTemplateWithID, ElementTemplate
from .model import T_model
from abc import ABC
from typing import Generic


class Element(ElementTemplate[T_model], ABC, Generic[T_model]):
    value: T_model

    def __init__(self, attributes: T_model) -> None:
        self.value = attributes


class ElementWithID(Element[T_model], ElementTemplateWithID[T_model], ABC, Generic[T_model]):
    @property
    def id(self) -> int:
        id_ = getattr(self.value, type(self).get_id_field_name(), None)

        if id_ is None:
            raise ValueError("check get_id_field_name(), it may not exist")

        if not isinstance(id_, int):
            raise TypeError("ID is not an integer")

        return id_
