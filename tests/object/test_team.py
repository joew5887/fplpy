import pytest
from fplpy.unlinked_object.team.object import UnlinkedTeam
from fplpy.unlinked_object.team.model import TeamModel


@pytest.fixture
def sample_team_1_model() -> TeamModel:
    """Fixture providing a sample TeamModel instance."""
    return TeamModel(**{
        "code":3,"draw":0,"id":1,"loss":0,"name":"Arsenal",
        "played":0,"points":0,"position":2,"short_name":"ARS","strength":5,
        "unavailable":False,"win":0,"strength_overall_home":1350,
        "strength_overall_away":1350,"strength_attack_home":1390,
        "strength_attack_away":1400,"strength_defence_home":1310,
        "strength_defence_away":1300,"pulse_id":1
    }
    )


@pytest.fixture
def sample_team_1(sample_team_1_model: TeamModel) -> UnlinkedTeam:
    """Fixture providing a sample Team instance."""
    return UnlinkedTeam(sample_team_1_model)


@pytest.fixture
def sample_team_2_model() -> TeamModel:
    """Fixture providing a sample TeamModel instance."""
    return TeamModel(**{
        "code":3,"draw":0,"form":None,"id":1,"loss":0,"name":"Arsenal",
        "played":0,"points":0,"position":2,"short_name":"ARS","strength":5,
        "unavailable":False,"win":0,"strength_overall_home":1350,
        "strength_overall_away":1350,"strength_attack_home":1390,
        "strength_attack_away":1400,"strength_defence_home":1310,
        "strength_defence_away":1300,"pulse_id":1
    }
    )


@pytest.fixture
def sample_team_2(sample_team_2_model: TeamModel) -> UnlinkedTeam:
    """Fixture providing a sample Team instance."""
    return UnlinkedTeam(sample_team_2_model)


def test_team_initialization(sample_team_1, sample_team_1_model) -> None:
    assert isinstance(sample_team_1, UnlinkedTeam)
    assert sample_team_1.value == sample_team_1_model
    assert sample_team_1.id == sample_team_1_model.code  # Ensuring correct ID mapping
    
    
def test_team_equality(sample_team_1, sample_team_1_model):
    another_team = UnlinkedTeam(sample_team_1_model)
    assert sample_team_1 == another_team  # Same attributes → should be equal


def test_team_hash(sample_team_1):
    expected_hash = hash((sample_team_1.id, sample_team_1.value.name))
    assert hash(sample_team_1) == expected_hash


def test_get_id_field_name():
    assert UnlinkedTeam.get_id_field_name() == "code"
