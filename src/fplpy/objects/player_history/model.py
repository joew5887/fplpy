from .._element.model import Model
from dataclasses import dataclass


@dataclass(frozen=True, order=True, kw_only=True)
class PlayerHistoryModel(Model):
    season_name: str
    element_code: int
    start_cost: int
    end_cost: int
    total_points: int
    minutes: int
    goals_scored: int
    assists: int
    clean_sheets: int
    goals_conceded: int
    own_goals: int
    penalties_saved: int
    penalties_missed: int
    yellow_cards: int
    red_cards: int
    saves: int
    bonus: int
    bps: int
    influence: float
    creativity: float
    threat: float
    ict_index: float
    defensive_contribution: int
    starts: int
    expected_goals: float
    expected_assists: float
    expected_goal_involvements: float
    expected_goals_conceded: float
