from typing import TypeAlias
from enum import Enum

# Objects
from .event.object import Event
from .fixture.object import Fixture
from .label.object import Label
from .player.object import Player
from .position.object import Position
from .team.object import Team
from .game_settings.object import GameSettings
from .player_summary.object import PlayerSummary
from .chip.object import Chip
from .player_history.object import PlayerHistory

# Repositories
from ..objects.event.repository import EventRepository
from ..objects.chip.repository import ChipRepository
from ..objects.fixture.repository import FixtureRepository
from ..objects.game_settings.repository import GameSettingsRepository
from ..objects.label.repository import LabelRepository
from ..objects.player.repository import PlayerRepository
from ..objects.position.repository import PositionRepository
from ..objects.team.repository import TeamRepository
from ..objects.player_summary.repository import PlayerSummaryRepository
from ..objects.player_history.repository import PlayerHistoryRepository


class ObjTypes:
    Chip: TypeAlias = Chip
    Event: TypeAlias = Event
    Fixture: TypeAlias = Fixture
    GameSettings: TypeAlias = GameSettings
    Label: TypeAlias = Label
    Player: TypeAlias = Player
    PlayerSummary: TypeAlias = PlayerSummary
    Position: TypeAlias = Position
    Team: TypeAlias = Team
    PlayerHistory: TypeAlias = PlayerHistory


class RepoTypes:
    ChipRepo: TypeAlias = ChipRepository[ObjTypes.Chip]
    EventRepo: TypeAlias = EventRepository[ObjTypes.Event]
    FixtureRepo: TypeAlias = FixtureRepository[ObjTypes.Fixture]
    GameSettingsRepo: TypeAlias = GameSettingsRepository[ObjTypes.GameSettings]
    LabelRepo: TypeAlias = LabelRepository[ObjTypes.Label]
    PlayerRepo: TypeAlias = PlayerRepository[ObjTypes.Player]
    PlayerSummaryRepo: TypeAlias = PlayerSummaryRepository[ObjTypes.PlayerSummary]
    PositionRepo: TypeAlias = PositionRepository[ObjTypes.Position]
    TeamRepo: TypeAlias = TeamRepository[ObjTypes.Team]
    PlayerHistoryRepo: TypeAlias = PlayerHistoryRepository[ObjTypes.PlayerHistory]
    

class ObjNames(str, Enum):
    EVENT = "event"
    FIXTURE = "fixture"
    LABEL = "label"
    PLAYER = "player"
    POSITION = "position"
    TEAM = "team"
    GAME_SETTINGS = "game_settings"
    CHIP = "chip"
    PLAYER_SUMMARY = "player_summary"
    PLAYER_HISTORY = "player_history"
