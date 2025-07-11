import pytest
import os

import fplpy

def main() -> None:
    ctx = fplpy.GitHubRepositoryFactory("2022-23")
    players = ctx.players()
    x = players.get_by_id(103955)

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


if __name__ == "__main__":
    main2()