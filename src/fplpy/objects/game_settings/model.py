from .._element.model import Model
from dataclasses import dataclass


@dataclass(frozen=True, order=True, kw_only=True)
class GameSettingsModel(Model):
    league_join_private_max: int
    league_join_public_max: int
    league_max_size_public_classic: int
    league_max_size_public_h2h: int
    league_max_size_private_h2h: int
    league_max_ko_rounds_private_h2h: int
    league_prefix_public: str
    league_points_h2h_win: int
    league_points_h2h_lose: int
    league_points_h2h_draw: int
    league_ko_first_instead_of_random: bool
    element_sell_at_purchase_price: bool
    underdog_differential: int
    squad_squadplay: int
    squad_squadsize: int
    squad_team_limit: int
    squad_total_spend: int
    transfers_cap: int
    transfers_sell_on_fee: float
    max_extra_free_transfers: int
    timezone: str
