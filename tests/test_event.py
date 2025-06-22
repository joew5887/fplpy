import pytest

from fplpy import PlayerGitHub, PlayerSummaryGitHub

season = "2022-23"

x = PlayerGitHub(season).get_all()[0]
print(x)
print(x.player_summary_df(PlayerSummaryGitHub, season))
