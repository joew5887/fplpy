import pytest
import os

import fplpy

def main() -> None:
    ctx = fplpy.GitHubRepositoryFactory("2022-23")
    players = ctx.players()
    x = players.get_by_code(103955)

    if x is None:
        return
    
    y = fplpy.PlayerEnricher(ctx)
    print(y.enrich(x))
    
    
def main2() -> None:
    ctx = fplpy.GitHubRepositoryFactory("2022-23")
    players = ctx.fixtures()
    x = players.get_all()[0]
    
    y = fplpy.FixtureEnricher(ctx)
    print(y.enrich(x))


def main3() -> None:
    path = os.path.join("src", "fplpy", "objects", "event", "external", "2024_25_local.txt")
    ctx = fplpy.RepositoryFactory202425(path)
    event = ctx.events().get_by_id(1)
    
    if event is not None:
        print(event.deadline_time)
    
    
def total_scores() -> None:
    repo_factory = fplpy.APIRepositoryFactory()
    events_repo = repo_factory.events()
    all_events = events_repo.get_all()
    
    total = 0
    best = 0
    for event in all_events:
        print(type(event).__hash__)
        if event.value.average_entry_score is not None and event.value.highest_score is not None:
            total += event.value.average_entry_score
            best += event.value.highest_score
            
    print(total)
    print(best)
    

if __name__ == "__main__":
    path = os.path.join("src", "fplpy", "objects", "event", "external", "2024_25_local.txt")
    c = fplpy.RepositoryFactory202425(path)
    player = c.players().get_filtered(lambda player: player.value.web_name == "Jake Evans")[0]
    engine = fplpy.PlayerEnricher(c)
    
    if player is not None:
        player_cost_tracker = fplpy.PlayerCostTracker.from_player(player, c)
    
        for event in c.events().get_all():
            print(event.id, player_cost_tracker.cost_at_event_begin(event, 1_000_000))
