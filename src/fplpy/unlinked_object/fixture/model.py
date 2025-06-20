from .._element.model import Model
from dataclasses import dataclass, field
from typing import Optional, Any


@dataclass(frozen=True, order=True, kw_only=True)
class FixtureModel(Model):
    kickoff_time: Optional[str]
    id: int
    event: int
    code: int
    finished: bool
    finished_provisional: bool
    minutes: int
    provisional_start_time: bool
    started: bool
    team_a: int
    team_a_score: Optional[int]
    team_h: int
    team_h_score: Optional[int]
    stats: list[dict[str, Any]] = field(default_factory=list)
    team_h_difficulty: int
    team_a_difficulty: int
    pulse_id: int
