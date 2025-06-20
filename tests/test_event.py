import pytest

from fplpy.repository import PlayerGitHub, TeamGitHub

season = "2022-23"
x = PlayerGitHub(season)

print(x.get_all()[0])
print(x.get_all()[0].team(TeamGitHub(season)))
