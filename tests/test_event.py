import pytest
import os

import fplpy

ctx = fplpy.GitHubRepositoryFactory("2022-23")
players = ctx.players()
x = players.get_filtered(lambda p: p.value.now_cost >= 90)
print(x)
"""
from fplpy import BaseFPLRepositoryFactory, APIPresetRepositoryFactory
from fplpy.repository_factory.general import RepoType, Source

season = "2022-23"
path = os.path.join("src", "fplpy", "unlinked_object", "event", "external", "2024_25_local.txt")

source = Source.GITHUB
player_repo = BaseFPLRepositoryFactory.players(source, season=season)
x = player_repo.get_all()[160]

y = BaseFPLRepositoryFactory.player_summary(Source.GITHUB, x, season=season)
print(y.as_df())

print()
"""