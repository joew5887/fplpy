import pytest
from .example_data import team_model, label_model, position_model, \
    player_model, fixture_model, event_model
from fplpy.unlinked_object.event.object import UnlinkedEvent
from fplpy.unlinked_object.fixture.object import UnlinkedFixture
from fplpy.unlinked_object.player.object import UnlinkedPlayer
from fplpy.unlinked_object.label.object import UnlinkedLabel
from fplpy.unlinked_object.position.object import UnlinkedPosition
from fplpy.unlinked_object.team.object import UnlinkedTeam

from fplpy.unlinked_object._element.element import ElementTemplate


@pytest.mark.parametrize(
    "object_cls, init_args, expected_str",
    [
        (UnlinkedTeam, {"attributes": team_model()}, "Arsenal"),
        (UnlinkedLabel, {"attributes": label_model()}, "Goals Scored"),
        (UnlinkedPosition, {"attributes": position_model()}, "Goalkeeper"),
        (UnlinkedPlayer, {"attributes": player_model()}, "Fábio Vieira"),
        (UnlinkedFixture, {"attributes": fixture_model()}, "14 v 9"),
        (UnlinkedEvent, {"attributes": event_model()}, "Gameweek 1")
    ]
)

def test_str(object_cls, init_args, expected_str) -> None:
    instance = object_cls(**init_args)
    
    assert str(instance) == expected_str
    #assert isinstance(instance, ElementTemplate)
    

@pytest.mark.parametrize(
    "object_cls, init_args, expected_repr",
    [
        (UnlinkedTeam, {"attributes": team_model()}, "Team(code(ID)=3, name='Arsenal')"),
        (UnlinkedLabel, {"attributes": label_model()}, "Label(label='Goals Scored', name='goals_scored')"),
        (UnlinkedPosition, {"attributes": position_model()}, "Position(id(ID)=1, singular_name='Goalkeeper', singular_name_short='GKP')"),
        (UnlinkedPlayer, {"attributes": player_model()}, "Player(code(ID)=438098, web_name='Fábio Vieira', team=1, position=3)"),
        (UnlinkedFixture, {"attributes": fixture_model()}, "Fixture(code(ID)=2444470, team_h=14, team_a=9, event=1)"),
        (UnlinkedEvent, {"attributes": event_model()}, "Event(id(ID)=1, name='Gameweek 1', deadline_time='2024-08-16T17:30:00Z')")
    ]
)
def test_repr(object_cls, init_args, expected_repr) -> None:
    instance = object_cls(**init_args)
    
    assert repr(instance) == expected_repr
    
    
@pytest.mark.parametrize(
    "object_cls, init_args",
    [
        (UnlinkedTeam, {"attributes": team_model()}),
        (UnlinkedLabel, {"attributes": label_model()}),
        (UnlinkedPosition, {"attributes": position_model()}),
        (UnlinkedPlayer, {"attributes": player_model()}),
        (UnlinkedFixture, {"attributes": fixture_model()}),
        (UnlinkedEvent, {"attributes": event_model()})
    ]
)
def test_eq_true(object_cls, init_args) -> None:
    instance_1 = object_cls(**init_args)
    instance_2 = object_cls(**init_args)
    
    assert instance_1 == instance_2
