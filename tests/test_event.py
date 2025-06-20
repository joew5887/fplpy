import pytest
from fplpy.linked_object.repository.player import PlayerAPI as LinkedAPI
from fplpy.linked_object.repository.team import TeamAPI as TeamAPI
from fplpy.unlinked_object.player.external.api import PlayerAPI as UnlinkedAPI

x = LinkedAPI()
y = UnlinkedAPI()
z = TeamAPI()

print(y.get_all()[0])
print(x.get_all()[0].team(z))
