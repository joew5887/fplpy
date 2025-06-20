import pytest

from fplpy.repository import PlayerGitHub, TeamGitHub

season = "2023-24"
x = PlayerGitHub(season)
y = TeamGitHub(season)

print(x.get_all()[0])
print(x.get_all()[0].team(y))
