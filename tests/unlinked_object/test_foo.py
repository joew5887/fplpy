import pytest
from .example_data import team_model, label_model, position_model, \
    player_model, fixture_model, event_model
from ..util.util import wrap_argument
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
        (UnlinkedTeam, wrap_argument(team_model()), "Arsenal"),
        (UnlinkedLabel, wrap_argument(label_model()), "Goals Scored"),
        (UnlinkedPosition, wrap_argument(position_model()), "Goalkeeper"),
        (UnlinkedPlayer, wrap_argument(player_model()), "Fábio Vieira"),
        (UnlinkedFixture, wrap_argument(fixture_model()), "14 v 9"),
        (UnlinkedEvent, wrap_argument(event_model()), "Gameweek 1")
    ]
)

def test_str(object_cls, init_args, expected_str) -> None:
    instance = object_cls(**init_args)
    
    assert str(instance) == expected_str
    #assert isinstance(instance, ElementTemplate)
    

@pytest.mark.parametrize(
    "object_cls, init_args, expected_repr",
    [
        (UnlinkedTeam, wrap_argument(team_model()), "Team(code(ID)=3, name='Arsenal')"),
        (UnlinkedLabel, wrap_argument(label_model()), "Label(label='Goals Scored', name='goals_scored')"),
        (UnlinkedPosition, wrap_argument(position_model()), "Position(id(ID)=1, singular_name='Goalkeeper', singular_name_short='GKP')"),
        (UnlinkedPlayer, wrap_argument(player_model()), "Player(code(ID)=438098, web_name='Fábio Vieira', team=1, position=3)"),
        (UnlinkedFixture, wrap_argument(fixture_model()), "Fixture(code(ID)=2444470, team_h=14, team_a=9, event=1)"),
        (UnlinkedEvent, wrap_argument(event_model()), "Event(id(ID)=1, name='Gameweek 1', deadline_time='2024-08-16T17:30:00Z')")
    ]
)
def test_repr(object_cls, init_args, expected_repr) -> None:
    instance = object_cls(**init_args)
    
    assert repr(instance) == expected_repr
    
    
@pytest.mark.parametrize(
    "object_cls, init_args",
    [
        (UnlinkedTeam, wrap_argument(team_model())),
        (UnlinkedLabel, wrap_argument(label_model())),
        (UnlinkedPosition, wrap_argument(position_model())),
        (UnlinkedPlayer, wrap_argument(player_model())),
        (UnlinkedFixture, wrap_argument(fixture_model())),
        (UnlinkedEvent, wrap_argument(event_model()))
    ]
)
def test_eq_true(object_cls, init_args) -> None:
    instance_1 = object_cls(**init_args)
    instance_2 = object_cls(**init_args)
    
    assert instance_1 == instance_2
