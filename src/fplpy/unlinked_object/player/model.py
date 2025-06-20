from .._element.model import Model
from typing import Any, Optional
from dataclasses import dataclass


@dataclass(frozen=True, order=True, kw_only=True)
class PlayerModel(Model):
    id: int
    chance_of_playing_next_round: Optional[int]
    chance_of_playing_this_round: Optional[int]
    code: int
    cost_change_event: int
    cost_change_event_fall: int
    cost_change_start: int
    cost_change_start_fall: int
    dreamteam_count: int
    element_type: int
    ep_next: float
    ep_this: float
    event_points: int
    first_name: str
    form: float
    in_dreamteam: bool
    news: str
    news_added: str
    now_cost: int
    photo: str
    points_per_game: float
    second_name: str
    selected_by_percent: float
    special: bool
    squad_number: Optional[int]
    status: str
    team: int
    team_code: int
    total_points: int
    transfers_in: int
    transfers_in_event: int
    transfers_out: int
    transfers_out_event: int
    value_form: float
    value_season: float
    web_name: str   # foo
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
    influence_rank: int
    influence_rank_type: int
    creativity_rank: int
    creativity_rank_type: int
    threat_rank: int
    threat_rank_type: int
    ict_index_rank: int
    ict_index_rank_type: int
    corners_and_indirect_freekicks_order: Optional[int]
    corners_and_indirect_freekicks_text: str
    direct_freekicks_order: Optional[int]
    direct_freekicks_text: str
    penalties_order: Optional[int]
    penalties_text: str
