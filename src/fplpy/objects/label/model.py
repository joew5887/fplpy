from .._element.model import Model
from dataclasses import dataclass


@dataclass(frozen=True, order=True, kw_only=True)
class LabelModel(Model):
    label: str  # Formal
    name: str  # Code
