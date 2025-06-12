from datetime import datetime
from typing import Generic, TypeVar, Union, Any
from .elements import Element, ElementGroup
from ..external.api import FPLAPI
from dataclasses import dataclass, field
from ..util.dt import string_to_datetime


base_event = TypeVar("base_event", bound="BaseEvent[Any]")


@dataclass(frozen=True, order=True, kw_only=True)
class BaseEvent(Element[base_event], Generic[base_event]):
    """Event / Gameweek element, unlinked from other FPL elements.
    """

    deadline_time: datetime = field(repr=False, hash=False)
    id: int = field(repr=False)

    name: str = field(hash=False, compare=False)
    average_entry_score: int = field(hash=False, repr=False, compare=False)
    finished: bool = field(hash=False, repr=False, compare=False)
    data_checked: bool = field(hash=False, repr=False, compare=False)
    highest_scoring_entry: int = field(hash=False, repr=False, compare=False)
    is_previous: bool = field(hash=False, repr=False, compare=False)
    is_current: bool = field(hash=False, repr=False, compare=False)
    is_next: bool = field(hash=False, repr=False, compare=False)
    cup_leagues_created: bool = field(hash=False, repr=False, compare=False)
    h2h_ko_matches_created: bool = field(hash=False, repr=False, compare=False)
    chip_plays: list[dict[str, Union[str, int]]
                     ] = field(hash=False, repr=False, compare=False)
    most_selected: Any = field(hash=False, repr=False, compare=False)
    most_transferred_in: Any = field(hash=False, repr=False, compare=False)
    top_element: Any = field(hash=False, repr=False, compare=False)
    top_element_info: dict[str, Any] = field(
        hash=False, repr=False, compare=False)
    transfers_made: int = field(hash=False, repr=False, compare=False)
    most_captained: Any = field(hash=False, repr=False, compare=False)
    most_vice_captained: Any = field(hash=False, repr=False, compare=False)
    
    @classmethod
    def from_dict_api(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        # converts string datetime to datetime object
        # TODO: regex support
        if element_args["deadline_time"] is not None:
            element_args["deadline_time"] = \
                string_to_datetime(element_args["deadline_time"])
        else:
            element_args["deadline_time"] = datetime.max

        return element_args
    
    @classmethod
    def from_dict_vaastav(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        return cls.from_dict_api(element_args)
    
    @classmethod
    def get_latest_external_data(cls, source: FPLAPI) -> list[dict[str, Any]]:
        data = source.get_events()

        # none gameweek
        data.append({
            "id": 0, "name": "No Gameweek", "deadline_time": None, "average_entry_score": 0,
            "finished": False, "data_checked": False, "highest_scoring_entry": 0, "is_previous": False,
            "is_current": False, "is_next": False, "cup_leagues_created": False, "h2h_ko_matches_created": False,
            "chip_plays": [], "most_selected": None, "most_transferred_in": None, "top_element": None,
            "top_element_info": dict(), "transfers_made": 0, "most_captained": None, "most_vice_captained": None
        })
        
        return data

    def __add__(self, other: int) -> base_event:
        """Increments the event by `other` gameweeks.

        Parameters
        ----------
        other : int
            Number of gameweeks to go up by.

        Returns
        -------
        event
            Event at gameweek `self.unique_id + other`.
            May be None if outside season.

        Raises
        ------
        NotImplementedError
            `other` must be an int.
        Exception
            ID added goes outside of gameweek range.
        """
        if not isinstance(other, int):
            raise NotImplementedError

        gw = type(self).get_by_id(self.unique_id + other)

        if gw is None:
            raise Exception("No gameweek found.")

        return gw

    def __iadd__(self, other: int) -> base_event:
        return self.__add__(other)

    def __sub__(self, other: int) -> base_event:
        """Decrements the event by `other` gameweeks.

        Parameters
        ----------
        other : int
            Number of gameweeks to go down by.

        Returns
        -------
        event
            Event at gameweek `self.unique_id - other`.
            May be None if outside season.

        Raises
        ------
        NotImplementedError
            `other` must be an int.
        """
        if not isinstance(other, int):
            raise NotImplementedError

        return self.__add__((-1) * other)

    def __isub__(self, other: int) -> base_event:
        return self.__sub__(other)

    @property
    def started(self) -> bool:
        """Has the gameweek started?

        Uses `datetime.now()`.

        Returns
        -------
        bool
            True if gameweek has started, False otherwise.
        """
        return datetime.now() > self.deadline_time

    @classmethod
    def range(cls, start_gw: base_event, start: int, end: int, step: int) -> ElementGroup[base_event]:
        """Gets a range of events between two points.

        Parameters
        ----------
        start_gw : _event
            Event to start list from, may be included in list if `start` = 0.
        start : int
            Where to start incrementing from.
        end : int
            Where to stop incrementing.
        step : int
            How much to increment by.
        Returns
        -------
        ElementGroup[event]
            Events in the range.

        Raises
        ------
        ValueError
            If the range produces an empty list.
        """
        group: list[base_event] = [
            start_gw.__add__(i) for i in range(start, end, step)]

        if len(group) == 0:
            raise ValueError("No gameweeks found")

        return ElementGroup[base_event](group)

    @classmethod
    def get_previous_gw(cls) -> base_event:
        """Returns the previous gameweek at the time of program execution.

        Returns
        -------
        event
            The previous gameweek.
        """
        return cls.__find_until_true("is_previous")

    @classmethod
    def get_current_gw(cls) -> base_event:
        """Returns current gameweek at the time of program execution.

        Returns
        -------
        event
            The current gameweek.
        """
        return cls.__find_until_true("is_current")

    @classmethod
    def get_next_gw(cls) -> base_event:
        """Returns the next gameweek at the time of program execution.

        Returns
        -------
        event
            The next gameweek.
        """
        return cls.__find_until_true("is_next")

    @classmethod
    def get_model_gw(cls) -> base_event:
        """Gameweek for model.

        Uses current gameweek.
        If it has finished, the next gameweek is returned.

        Returns
        -------
        _event
            Model gw.
        """
        current_gw = cls.get_current_gw()
        next_gw = cls.get_next_gw()

        if current_gw.finished:
            return next_gw

        return current_gw

    @classmethod
    def past_and_future(cls) -> tuple[ElementGroup[base_event], ElementGroup[base_event]]:
        """Splits all the gameweeks into two groups by whether they have finished.

        Returns
        -------
        tuple[ElementGroup[event], ElementGroup[event]]
            The first group is the completed gameweeks, with the rest in group 2.
        """
        all_events = cls.get_scheduled_events()

        return all_events.split(finished=True)

    @classmethod
    def __find_until_true(cls, attr: str) -> base_event:
        """Iterates through all gameweeks until the attribute is True.

        Parameters
        ----------
        attr : str
            The boolean attribute to find.

        Returns
        -------
        event
            The first gameweek where the attribute is True, may be no gameweek if they are all False.
        """
        all_events = cls.get_all()

        for event in all_events:
            if getattr(event, attr):
                return event

        return cls.none()

    @classmethod
    def none(cls) -> base_event:
        """Default no gameweek Event element.

        Used for fixtures that have been postponed and not rearranged to another gameweek.

        Returns
        -------
        _event
            No gameweek event.
        """
        return cls.get(id=0)[0]

    @classmethod
    def get_scheduled_events(cls) -> ElementGroup[base_event]:
        """Get all events, except the no gameweek element.

        Returns
        -------
        ElementGroup[_event]
            `cls.get_all()` except `cls.none()`.
        """
        all_events = cls.get_all()

        return ElementGroup[base_event]([event for event in all_events if event != cls.none()])


@dataclass(frozen=True, order=True, kw_only=True)
class UnlinkedEvent(BaseEvent["UnlinkedEvent"]):
    """Independent Event element, not linked to any other FPL elements.
    """
    most_selected: int = field(hash=False, repr=False, compare=False)
    most_transferred_in: int = field(hash=False, repr=False, compare=False)
    top_element: int = field(hash=False, repr=False, compare=False)
    top_element_info: dict[str, int] = field(
        hash=False, repr=False, compare=False)
    most_captained: int = field(hash=False, repr=False, compare=False)
    most_vice_captained: int = field(hash=False, repr=False, compare=False)
