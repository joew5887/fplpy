from __future__ import annotations
from dataclasses import dataclass
from .elements import Element
from ..external.api import FPLAPI
from typing import Any


@dataclass(frozen=True, order=True, kw_only=True)
class Label(Element["Label"]):
    """Name for FPL player attribute.
    """
    UNIQUE_ID_ATTR = "name"
    STR_ATTR= "label"

    label: str
    name: str
    
    @classmethod
    def from_dict_api(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        return element_args
    
    @classmethod
    def from_dict_vaastav(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        return element_args

    @classmethod
    def get_latest_external_data(cls, source: FPLAPI) -> list[dict[str, Any]]:
        data = source.get_labels()
        
        # New player labels
        data.append({"label": "Goal Contributions",
                    "name": "goal_contributions"})
        data.append({"label": "Percent Position",
                    "name": "percent_pos"})
        data.append({"label": "Percent Team",
                    "name": "percent_team"})
        data.append({"label": "Total Points", "name": "total_points"})
        data.append({"label": "Transfers in for next Gameweek", "name": "transfers_in_event"})
        data.append({"label": "Transfers out for next Gameweek", "name": "transfers_out_event"})
        
        return data
