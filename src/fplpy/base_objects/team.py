from typing import TypeVar, Generic, Any
from .elements.element import Element
from ..external.template import ExternalFPLData
from ..external.api import FPLAPI
from ..external.github import VaastavGitHub
from dataclasses import dataclass, field


_team = TypeVar("_team", bound="BaseTeam[Any]")


@dataclass(frozen=True, order=True, kw_only=True)
class BaseTeam(Element[_team], Generic[_team]):
    """Element for team in the Premier League, unlinked from other FPL elements.
    """
    id: int = field(repr=False)
    code: int = field(repr=False)

    draw: int = field(hash=False, repr=False, compare=False)
    form: None = field(hash=False, repr=False, compare=False)
    loss: int = field(hash=False, repr=False, compare=False)
    name: str = field(hash=False, compare=False)
    played: int = field(hash=False, repr=False, compare=False)
    points: int = field(hash=False, repr=False, compare=False)
    position: int = field(hash=False, repr=False, compare=False)
    short_name: str = field(hash=False, repr=False, compare=False)
    strength: int = field(hash=False, repr=False, compare=False)
    team_division: None = field(hash=False, repr=False, compare=False)
    unavailable: bool = field(hash=False, repr=False, compare=False)
    win: int = field(hash=False, repr=False, compare=False)
    strength_overall_home: int = field(hash=False, repr=False, compare=False)
    strength_overall_away: int = field(hash=False, repr=False, compare=False)
    strength_attack_home: int = field(hash=False, repr=False, compare=False)
    strength_attack_away: int = field(hash=False, repr=False, compare=False)
    strength_defence_home: int = field(hash=False, repr=False, compare=False)
    strength_defence_away: int = field(hash=False, repr=False, compare=False)
    pulse_id: int = field(repr=False, compare=False)

    @classmethod
    def from_dict_api(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        return element_args
    
    @classmethod
    def from_dict_vaastav(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        return element_args

    @classmethod
    def get_latest_external_data(cls, source: ExternalFPLData) -> list[dict]:
        return source.get_teams()

    @classmethod
    def get_all_names(cls) -> list[str]:
        """All team names in the Premier League.

        Returns
        -------
        list[str]
            E.g. ['Arsenal', 'Aston Villa', ...]
        """
        all_teams = cls.get()

        return all_teams.to_string_list()
