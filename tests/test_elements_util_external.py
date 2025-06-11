from typing import Any
import pytest
from fplpy.external.api import FPLAPI
from fplpy.external.github import VaastavGitHub, github_csv_to_dict
from fplpy.base_objects.team import BaseTeam
from fplpy.base_objects.fixture import BaseFixture
from fplpy.base_objects.player import BasePlayer
from fplpy import Event as BaseEvent
from fplpy import Label
from fplpy import Position
from dataclasses import fields


EXPECTED_TOTAL_GAMEWEEKS = 38
EXPECTED_TOTAL_TEAMS = 20
EXPECTED_TOTAL_FIXTURES = 380
EXPECTED_TOTAL_POSITIONS = 5  # GKP, DEF, MID, FWD, MNG


def all_field_names(class_) -> list[str]:
    """Gets all field names for a given class.

    Parameters
    ----------
    class_ : _type_
        A class with the `@dataclass` decorator.

    Returns
    -------
    list[str]
        All field names for `class_`.
    """
    class_attrs = fields(class_)

    return [attr.name for attr in class_attrs]


def assert_output_has_required_attributes(data: list[dict], class_) -> None:
    team_cls_fields = set(all_field_names(class_))
        
    for item in data:
        assert team_cls_fields.issubset(set(item.keys()))


class TestFPLAPI:
    def test_get_teams(self) -> None:
        source = FPLAPI()
        data = source.get_teams()
        
        assert_output_has_required_attributes(data, BaseTeam)
        assert len(data) == EXPECTED_TOTAL_TEAMS
            
    def test_get_fixtures(self) -> None:
        source = FPLAPI()
        data = source.get_fixtures()
        
        assert_output_has_required_attributes(data, BaseFixture)
        assert len(data) == EXPECTED_TOTAL_FIXTURES
            
    def test_get_players(self) -> None:
        source = FPLAPI()
        data = source.get_players()
        
        assert_output_has_required_attributes(data, BasePlayer)
            
    def test_get_events(self) -> None:
        source = FPLAPI()
        data = source.get_events()
        
        assert_output_has_required_attributes(data, BaseEvent)
        assert len(data) == EXPECTED_TOTAL_GAMEWEEKS
            
    def test_get_labels(self) -> None:
        source = FPLAPI()
        data = source.get_labels()
        
        assert_output_has_required_attributes(data, Label)
            
    def test_get_positions(self) -> None:
        source = FPLAPI()
        data = source.get_positions()
        
        assert_output_has_required_attributes(data, Position)
        assert len(data) == EXPECTED_TOTAL_POSITIONS
            

class TestVaastavGitHub202425:
    SEASON = "2024-25"
    
    def test_get_teams(self) -> None:
        source = VaastavGitHub(type(self).SEASON)
        data = source.get_teams()
        
        assert_output_has_required_attributes(data, BaseTeam)
        assert len(data) == EXPECTED_TOTAL_TEAMS
            
    def test_get_fixtures(self) -> None:
        source = VaastavGitHub(type(self).SEASON)
        data = source.get_fixtures()
        
        assert_output_has_required_attributes(data, BaseFixture)
        assert len(data) == EXPECTED_TOTAL_FIXTURES

    def test_get_players(self) -> None:
        source = VaastavGitHub(type(self).SEASON)
        data = source.get_players()

        assert_output_has_required_attributes(data, BasePlayer)
        

class TestVaastavGitHub202324(TestVaastavGitHub202425):
    SEASON = "2023-24"
    

class TestVaastavGitHub202223(TestVaastavGitHub202425):
    SEASON = "2022-23"
    

class TestVaastavGitHub202122(TestVaastavGitHub202425):
    SEASON = "2021-22"
    

class TestVaastavGitHub202021(TestVaastavGitHub202425):
    SEASON = "2020-21"
    
    
# 2019-20 and below do not work with this package
        
        
def test_invalid_github_csv_to_dict() -> None:
    invalid_url = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/2024-25/foo.csv"
    
    with pytest.raises(Exception):
        github_csv_to_dict(invalid_url)
