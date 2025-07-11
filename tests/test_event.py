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
    total_scores()
