from typing import Any, Literal
import requests
from json import loads
from functools import cache


@cache
def __call_api(url_link: str) -> Any:
    response = requests.get(url_link)
    utf8 = response.text.encode("utf8")
    json_data = utf8.decode("unicode_escape")

    return loads(json_data)


def call_api(url_link: str) -> Any:
    return __call_api(url_link)


FPL_URL_STEM = "https://fantasy.premierleague.com/api/"
SUB_FPL_URLS = {
    "EVENTS": "events/",
    "BOOTSTRAP-STATIC": "bootstrap-static/",
    "FIXTURES": "fixtures/",
    "ELEMENT-SUMMARY": "element-summary/{}/",
}


def get_element_summary_url(player_id: int) -> str:
    return FPL_URL_STEM + SUB_FPL_URLS["ELEMENT-SUMMARY"].format(player_id)


def get_url(key: Literal["EVENTS", "BOOTSTRAP-STATIC", "FIXTURES"]) -> str:
    return FPL_URL_STEM + SUB_FPL_URLS[key]
