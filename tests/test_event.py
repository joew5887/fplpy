import pytest

from fplpy import PlayerAPI, PlayerSummaryAPI

season = "2023-24"

x = PlayerAPI.get_all()[0]
print(x.player_summary_df(PlayerSummaryAPI))
