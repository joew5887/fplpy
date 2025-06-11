import requests
import csv
from typing import Literal, Any
from .template import ExternalFPLData


DEFAULT_SEASON = "2024-25"


class VaastavGitHub(ExternalFPLData):
    def __init__(self, season: str = DEFAULT_SEASON):
        self.__season = season

    def get_teams(self) -> list[dict[str, Any]]:
        url = get_vaastav_url("TEAMS", self.__season)
        output: list[dict[str, Any]] = github_csv_to_dict(url)

        return output

    def get_fixtures(self) -> list[dict[str, Any]]:
        url = get_vaastav_url("FIXTURES", self.__season)
        output: list[dict[str, Any]] = github_csv_to_dict(url)

        return output

    def get_players(self) -> list[dict[str, Any]]:
        url = get_vaastav_url("PLAYERS", self.__season)
        output: list[dict[str, Any]] = github_csv_to_dict(url)

        return output


def github_csv_to_dict(csv_url: str) -> list[dict[Any, Any]]:
    """Fetches a CSV file from GitHub and returns it as a JSON dictionary."""
    response = requests.get(csv_url)

    if response.status_code == 200:
        decoded_content = response.content.decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_content)
        data = [row for row in reader]

        return data  # Returning the JSON-like dictionary
    else:
        raise Exception(f"Failed to fetch CSV: {response.status_code}")


VAASTAV_URL_STEM = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/refs/heads/master/"
SUB_VAASTAV_URLS = {
    "TEAMS": "data/{}/teams.csv",
    "FIXTURES": "data/{}/fixtures.csv",
    "PLAYERS": "data/{}/players_raw.csv",
}


def get_vaastav_url(key: Literal["TEAMS", "FIXTURES", "PLAYERS"], season: str) -> str:
    return VAASTAV_URL_STEM + SUB_VAASTAV_URLS[key].format(season)
