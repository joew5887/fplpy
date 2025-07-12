import pytest
from .example_data import team_model, label_model, position_model, \
    player_model, fixture_model, event_model
from ..util.util import wrap_argument
from fplpy.objects.event.object import Event
from fplpy.objects.fixture.object import Fixture
from fplpy.objects.player.object import Player
from fplpy.objects.label.object import Label
from fplpy.objects.position.object import Position
from fplpy.objects.team.object import Team


@pytest.mark.parametrize(
    "object_cls, init_args, expected_str",
    [
        (Team, wrap_argument(team_model()), "Arsenal"),
        (Label, wrap_argument(label_model()), "Goals Scored"),
        (Position, wrap_argument(position_model()), "Goalkeeper"),
        (Player, wrap_argument(player_model()), "Fábio Vieira"),
        (Fixture, wrap_argument(fixture_model()), "(Team 14) 1 - 0 (Team 9)"),
        (Event, wrap_argument(event_model()), "Gameweek 1")
    ]
)

def test_str(object_cls, init_args, expected_str) -> None:
    instance = object_cls(**init_args)
    
    assert str(instance) == expected_str
    

@pytest.mark.parametrize(
    "object_cls, init_args, expected_repr",
    [
        (Team, wrap_argument(team_model()), "Team(ID=1, CODE=3, name='Arsenal')"),
        (Label, wrap_argument(label_model()), "Label(label='Goals Scored', name='goals_scored')"),
        (Position, wrap_argument(position_model()), "Position(ID=1, singular_name='Goalkeeper', singular_name_short='GKP')"),
        (Player, wrap_argument(player_model()), "Player(ID=1, CODE=438098, web_name='Fábio Vieira', team=1, position=3)"),
        (Fixture, wrap_argument(fixture_model()), "Fixture(ID=1, CODE=2444470, team_h=14, team_a=9, event=1)"),
        (Event, wrap_argument(event_model()), "Event(ID=1, name='Gameweek 1', deadline_time='2024-08-16T17:30:00Z')")
    ]
)
def test_repr(object_cls, init_args, expected_repr) -> None:
    instance = object_cls(**init_args)
    
    assert repr(instance) == expected_repr
    
    
@pytest.mark.parametrize(
    "object_cls, init_args",
    [
        (Team, wrap_argument(team_model())),
        (Label, wrap_argument(label_model())),
        (Position, wrap_argument(position_model())),
        (Player, wrap_argument(player_model())),
        (Fixture, wrap_argument(fixture_model())),
        (Event, wrap_argument(event_model()))
    ]
)
def test_eq_true(object_cls, init_args) -> None:
    instance_1 = object_cls(**init_args)
    instance_2 = object_cls(**init_args)
    
    assert instance_1 == instance_2

@pytest.mark.parametrize(
    "object_cls, init_args",
    [
        (Team, wrap_argument(team_model())),
        (Label, wrap_argument(label_model())),
        (Position, wrap_argument(position_model())),
        (Player, wrap_argument(player_model())),
        (Fixture, wrap_argument(fixture_model())),
        (Event, wrap_argument(event_model()))
    ]
)
def test_hash(object_cls, init_args) -> None:
    instance = object_cls(**init_args)
    instance_hashed = hash(instance)
