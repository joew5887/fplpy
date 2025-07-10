from .repository_factory.general import BaseFPLRepositoryFactory, Source
from .objects.summary import Objects
from .objects.player_summary.repository import PlayerSummaryRepository
from typing import Optional

class FPLDataContext:
    def __init__(self, source: Source, **kwargs):
        self.source = source

        self.team_repo = BaseFPLRepositoryFactory.teams(self.source, **kwargs)
        self.player_repo = BaseFPLRepositoryFactory.players(self.source, **kwargs)
        self.fixture_repo = BaseFPLRepositoryFactory.fixtures(self.source, **kwargs)
        self.position_repo = BaseFPLRepositoryFactory.positions(self.source, **kwargs)
        self.label_repo = BaseFPLRepositoryFactory.labels(self.source, **kwargs)
        self.chip_repo = BaseFPLRepositoryFactory.chips(self.source, **kwargs)
        self.game_settings_repo = BaseFPLRepositoryFactory.game_settings(self.source, **kwargs)
        self.event_repo = BaseFPLRepositoryFactory.events(self.source, **kwargs)
        self.player_summary_repo_factory = lambda player: BaseFPLRepositoryFactory.player_summary(self.source, player, **kwargs)

    def get_team_for_player(self, player: Types.Player) -> Types.Team:
        res = self.team_repo.get_filtered(lambda x: x.value.id == player.value.team)

        return Types.Team(res[0].value)

    def get_position_for_player(self, player: Types.Player) -> Optional[Types.Position]:
        return self.position_repo.get_by_id(player.value.element_type)

    def get_event_for_fixture(self, fixture: Types.Fixture) -> Optional[Types.Event]:
        return self.event_repo.get_by_id(fixture.value.event)

    def get_home_team_for_fixture(self, fixture: Types.Fixture) -> Optional[Types.Team]:
        return self.team_repo.get_by_id(fixture.value.team_h)

    def get_away_team_for_fixture(self, fixture: Types.Fixture) -> Optional[Types.Team]:
        return self.team_repo.get_by_id(fixture.value.team_a)