from __future__ import annotations
import math
from typing import Any, Optional, Union
from .util.dt import datetime_to_string
from .base_objects.team import BaseTeam
from .base_objects.player import BasePlayer
from .base_objects.fixture import BaseFixture
from .base_objects.event import BaseEvent
from .base_objects.position import Position
from dataclasses import dataclass, field
from .base_objects.elements.element import ElementGroup


@dataclass(frozen=True, order=True, kw_only=True)
class LinkedTeam(BaseTeam["LinkedTeam"]):
    @property
    def fixture_score(self) -> float:
        """Gives a score for how hard upcoming fixtures are.

        Returns
        -------
        float
            The higher the score, the harder the fixtures.
        """
        all_fixtures = self.get_all_fixtures()
        fixtures_to_play = LinkedFixture.split_fixtures_by_finished(all_fixtures)[1]
        all_fixtures_by_event = LinkedFixture.group_fixtures_by_gameweek(
            fixtures_to_play)

        score: float = 0.0
        multiplier: float = 0.9

        i = 0
        for fixtures in all_fixtures_by_event.values():
            fixture: LinkedFixture
            for fixture in fixtures:
                diff = fixture.get_difficulty(self)

                score += diff * multiplier
                multiplier = math.e ** (-0.4 * i)
                i += 1

        return score

    @property
    def players(self) -> ElementGroup[LinkedPlayer]:
        """Get all players for a team.

        Returns
        -------
        ElementGroup[Player]
            Unsorted group of all players for a team.
        """
        return LinkedPlayer.get(team=self.unique_id)

    '''def average_form(self) -> float:
        """Gets average form of playing players in a team.

        Returns
        -------
        float
            Non-rounded average of team form.
        """
        eligible_players: list[Player] = []
        for player in self.players:
            player_full = player.in_full()

            if len(player_full.history.minutes.values) == 0:
                continue

            if player_full.history.minutes.values[-1] > 0:
                eligible_players.append(player)

        form_sum = sum(p.form for p in eligible_players)

        return form_sum / len(eligible_players)'''

    def get_all_fixtures(self) -> ElementGroup[LinkedFixture]:
        """Gets all fixtures and results for a team.

        Returns
        -------
        ElementGroup[fixture]
            Team fixtures and results sorted by kickoff time.
        """
        return LinkedFixture.get_all_team_fixtures(self.unique_id)

    def players_by_pos(self, position: Position) -> ElementGroup[LinkedPlayer]:
        """Gets all players from a team in a certain position.

        Parameters
        ----------
        position : Position
            Position to filter by.

        Returns
        -------
        ElementGroup[Player]
            All players from the team that play in that position.
        """
        return self.players.filter(element_type=position)

    def player_total(self, *cols: str, by_position: Optional[Position] = None) -> float:
        """Total points for all the players in a team, for a given attribute.

        Parameters
        ----------
        by_position : Optional[Position], optional
            Position to filter, None means all positions, by default None

        Returns
        -------
        float
            Total points.

        Raises
        ------
        AttributeError
            Attribute must exist in 'Player' fields.
        AttributeError
            Attribute found must be of type 'int' or 'float'.
        """
        if by_position is not None:
            players = self.players_by_pos(by_position)
        else:
            players = self.players

        total = 0.0

        player: LinkedPlayer
        for player in players:
            for col in cols:
                try:
                    value = getattr(player, col)
                except AttributeError:
                    raise AttributeError(f"Attribute, '{col}', doesn't exist.")
                else:
                    if not isinstance(value, (float, int)):
                        raise AttributeError(
                            f"'{col}' must return float or int value.")

                total += float(value)

        return total

    def total_goal_contributions(self, *, by_position: Optional[Position] = None) -> int:
        """Total goal contributions for a team.

        Parameters
        ----------
        by_position : Optional[Position], optional
            Position to filter, None means all positions, by default None

        Returns
        -------
        int
            Total goals + total assists.
        """
        cols = ["goals_scored", "assists"]

        return int(self.player_total(*cols, by_position=by_position))


@dataclass(frozen=True, order=True, kw_only=True)
class LinkedPlayer(BasePlayer["LinkedPlayer"]):
    """Player element, linked to other FPL elements.
    """
    team: LinkedTeam = field(hash=False, compare=False)
    element_type: Position = field(hash=False, compare=False)
    
    @classmethod
    def from_dict_api(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        super().from_dict_api(element_args)

        element_args["element_type"] = Position.get_by_id(
            element_args["element_type"])
        element_args["team"] = LinkedTeam.get_by_id(element_args["team"])

        return element_args


@dataclass(frozen=True, order=True, kw_only=True)
class LinkedEvent(BaseEvent["LinkedEvent"]):
    """Event / gameweek element, linked to other FPL elements.
    """
    most_selected: LinkedPlayer = field(hash=False, repr=False, compare=False)
    most_transferred_in: LinkedPlayer = field(hash=False, repr=False, compare=False)
    top_element: LinkedPlayer = field(hash=False, repr=False, compare=False)
    most_captained: LinkedPlayer = field(hash=False, repr=False, compare=False)
    most_vice_captained: LinkedPlayer = field(hash=False, repr=False, compare=False)
    
    @classmethod
    def from_dict_api(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        super().from_dict_api(element_args)
        
        element_args["most_selected"] = \
            LinkedPlayer.get_by_id(element_args["most_selected"])
        element_args["most_transferred_in"] = \
            LinkedPlayer.get_by_id(element_args["most_transferred_in"])
        element_args["top_element"] = \
            LinkedPlayer.get_by_id(element_args["top_element"])
        element_args["most_captained"] = \
            LinkedPlayer.get_by_id(element_args["most_captained"])
        element_args["most_vice_captained"] = \
            LinkedPlayer.get_by_id(element_args["most_vice_captained"])

        return element_args

    @property
    def fixtures(self) -> ElementGroup[LinkedFixture]:
        """Get all fixtures / results from a gameweek.

        Returns
        -------
        ElementGroup[Fixture]
            Unordered list of fixtures in gameweek.
        """
        return LinkedFixture.get(event=self)


@dataclass(frozen=True, order=True, kw_only=True)
class LinkedFixture(BaseFixture["LinkedFixture"]):
    """Fixture / result element, linked to other FPL elements.
    """
    event: LinkedEvent = field(hash=False, compare=False)
    team_h: LinkedTeam = field(hash=False, compare=False)
    team_a: LinkedTeam = field(hash=False, compare=False)

    @classmethod
    def from_dict_api(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        super().from_dict_api(element_args)
        
        element_args["event"] = LinkedEvent.get_by_id(element_args["event"])
        element_args["team_h"] = LinkedTeam.get_by_id(element_args["team_h"])
        element_args["team_a"] = LinkedTeam.get_by_id(element_args["team_a"])

        return element_args

    def get_difficulty(self, team: Union[int, LinkedTeam]) -> int:
        """Gets the difficulty of a fixture for a team.

        Parameters
        ----------
        team : Union[int, Team]
            Team to find difficulty for.

        Returns
        -------
        int
            Difficulty of the game for `team`.

        Raises
        ------
        ValueError
            If `team` is not in fixture.
        """
        if isinstance(team, LinkedTeam):
            team_id = team.unique_id
        else:
            team_id = team

        if self.team_h.unique_id == team_id:
            return self.team_h_difficulty
        elif self.team_a.unique_id == team_id:
            return self.team_a_difficulty
        else:
            raise ValueError(
                f"Team '{team}' not in fixture, '{str(self)}'")

    def is_home(self, team: Union[int, LinkedTeam]) -> bool:
        """Determines whether team passed is at home or away.

        Parameters
        ----------
        team : Union[int, Team]
            Team to find home or away for.

        Returns
        -------
        bool
            True if home, False otherwise.

        Raises
        ------
        ValueError
            If `team` is not in fixture.
        """
        if isinstance(team, LinkedTeam):
            team_id = team.unique_id
        else:
            team_id = team

        if self.team_h.unique_id == team_id:
            return True
        elif self.team_a.unique_id == team_id:
            return False
        else:
            raise ValueError(
                f"Team '{team}' not in fixture, '{str(self)}'")
