from .._element.model import Model
from typing import Optional
from dataclasses import dataclass, field


@dataclass
class ChipPlay:
    chip_name: str
    num_played: int


@dataclass(frozen=True, order=True, kw_only=True)
class EventModel(Model):
    id: int
    name: str
    deadline_time: Optional[str]
    finished: bool
    data_checked: bool
    average_entry_score: Optional[int]
    highest_score: Optional[int]
    is_previous: bool
    is_current: bool
    is_next: bool
    chip_plays: list[ChipPlay] = field(default_factory=list)
    most_selected: Optional[int]
    most_transferred_in: Optional[int]
    top_element: Optional[int]
    transfers_made: Optional[int]
    most_captained: Optional[int]
    most_vice_captained: Optional[int]
