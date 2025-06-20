import pytest
from fplpy.linked_object.repository.player import PlayerAPI as LinkedAPI
from fplpy.linked_object.repository.team import TeamAPI as TeamAPI
from fplpy.unlinked_object.player.external.api import PlayerAPI as UnlinkedAPI

from fplpy.linked_object.repository.player import PlayerGitHub as LinkedGitHub
from fplpy.linked_object.repository.team import TeamGitHub as TeamGitHub
from fplpy.unlinked_object.player.external.github import PlayerGitHub as UnlinkedGitHub

season = "2022-23"
x = LinkedGitHub(season=season)
y = UnlinkedGitHub(season=season)
z = TeamGitHub(season=season)

print(y.get_all()[0])
print(x.get_all()[0].team(z))
