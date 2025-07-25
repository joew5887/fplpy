from typing import Any, Literal
import requests
import csv
from functools import cache


@cache
def __github_csv_to_dict(csv_url: str) -> list[dict[Any, Any]]:
    """Fetches a CSV file from GitHub and returns it as a JSON dictionary."""
    response = requests.get(csv_url)

    if response.status_code == 200:
        decoded_content = response.content.decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_content)
        data = [row for row in reader]

        return data  # Returning the JSON-like dictionary
    else:
        raise Exception(f"Failed to fetch CSV: {response.status_code}")


def github_csv_to_dict(csv_url: str) -> list[dict[Any, Any]]:
    return __github_csv_to_dict(csv_url)


VAASTAV_URL_STEM = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/data/"
SUB_VAASTAV_URLS = {
    "TEAMS": "{}/teams.csv",
    "FIXTURES": "{}/fixtures.csv",
    "PLAYERS": "{}/players_raw.csv",
    "ELEMENT-SUMMARY": "{}/players/{}/gw.csv",
    "ELEMENT-HISTORY": "{}/players/{}/history.csv"
}


def format_player_name(first_name: str, second_name: str, player_id: int) -> str:
    return f"{first_name}_{second_name}_{player_id}"


def get_element_summary_url(season: str, player_name_formatted: str) -> str:
    return VAASTAV_URL_STEM + SUB_VAASTAV_URLS["ELEMENT-SUMMARY"].format(season, player_name_formatted)


def get_element_history_url(season: str, player_name_formatted: str) -> str:
    return VAASTAV_URL_STEM + SUB_VAASTAV_URLS["ELEMENT-HISTORY"].format(season, player_name_formatted)


def get_vaastav_url(key: Literal["TEAMS", "FIXTURES", "PLAYERS"], season: str) -> str:
    return VAASTAV_URL_STEM + SUB_VAASTAV_URLS[key].format(season)
