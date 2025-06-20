from .._element.model import Model
from dataclasses import dataclass, field


@dataclass(frozen=True, order=True, kw_only=True)
class PositionModel(Model):
    id: int
    plural_name: str
    plural_name_short: str
    singular_name: str
    singular_name_short: str
    squad_select: int
    squad_min_play: int
    squad_max_play: int
    ui_shirt_specific: bool
    sub_positions_locked: list[int] = field(default_factory=list)
    element_count: int
