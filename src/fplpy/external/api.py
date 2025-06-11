from .template import ExternalFPLData
from typing import Any, Literal
from json import loads
import requests


class FPLAPI(ExternalFPLData):
    def get_teams(self) -> list[dict[str, Any]]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))

        return data["teams"]

    def get_fixtures(self) -> list[dict[str, Any]]:
        data: list[dict[str, Any]] = call_api(get_url("FIXTURES"))

        return data

    def get_players(self) -> list[dict[str, Any]]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))

        return data["elements"]

    def get_events(self) -> list[dict[str, Any]]:
        data: list[dict[str, Any]] = call_api(get_url("EVENTS"))

        return data

    def get_labels(self) -> list[dict[str, Any]]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))

        return data["element_stats"]

    def get_positions(self) -> list[dict[str, Any]]:
        data: dict[str, list[dict[str, Any]]] = call_api(get_url("BOOTSTRAP-STATIC"))

        return data["element_types"]


def call_api(url_link: str) -> Any:
    response = requests.get(url_link)
    utf8 = response.text.encode("utf8")
    json_data = utf8.decode("unicode_escape")

    return loads(json_data)


FPL_URL_STEM = "https://fantasy.premierleague.com/api/"
SUB_FPL_URLS = {
    "EVENTS": "events/",
    "BOOTSTRAP-STATIC": "bootstrap-static/",
    "FIXTURES": "fixtures/"
}


def get_url(key: Literal["EVENTS", "BOOTSTRAP-STATIC", "ELEMENT-SUMMARY", "FIXTURES"]) -> str:
    return FPL_URL_STEM + SUB_FPL_URLS[key]
