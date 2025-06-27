import pytest
import os

from fplpy import EventLocal2425

season = "2022-23"

#x = PlayerGitHub(season).get_all()[0]
#print(x)
#print(x.player_summary_df(PlayerSummaryGitHub, season))
#src\fplpy\unlinked_object\event\external\2024_25_local.txt
path = os.path.join("src", "fplpy", "unlinked_object", "event", "external", "2024_25_local.txt")
y = EventLocal2425(path).get_all()[0]
print(EventLocal2425(path).get_next_event(y))
