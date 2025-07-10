from .._element.model import Model
from dataclasses import dataclass


@dataclass(frozen=True, order=True, kw_only=True)
class ChipModel(Model):
    id: int
    name: str
    number: int
    start_event: int
    stop_event: int
    chip_type: str
    #overrides": {
    #element_types
