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


class RepoTypes:
    Chip: TypeAlias = ChipRepository[ObjTypes.Chip]
    Event: TypeAlias = EventRepository[ObjTypes.Event]
    Fixture: TypeAlias = FixtureRepository[ObjTypes.Fixture]
    GameSettings: TypeAlias = GameSettingsRepository[ObjTypes.GameSettings]
    Label: TypeAlias = LabelRepository[ObjTypes.Label]
    Player: TypeAlias = PlayerRepository[ObjTypes.Player]
    PlayerSummary: TypeAlias = PlayerSummaryRepository[ObjTypes.PlayerSummary]
    Position: TypeAlias = PositionRepository[ObjTypes.Position]
    Team: TypeAlias = TeamRepository[ObjTypes.Team]
    

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
