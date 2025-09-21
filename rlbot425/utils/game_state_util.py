from dataclasses import dataclass
from typing import TypeAlias

from rlbot import flat

Rotator: TypeAlias = flat.RotatorPartial
Vector3: TypeAlias = flat.Vector3Partial
Physics: TypeAlias = flat.DesiredPhysics
BallState: TypeAlias = flat.DesiredBallState


@dataclass(init=False, slots=True)
class CarState:
    physics: Physics | None
    boost_amount: float | None
    jumped: bool | None
    double_jumped: bool | None

    def __init__(
        self,
        physics: Physics | None = None,
        boost_amount: float | None = None,
        jumped: bool | None = None,
        double_jumped: bool | None = None,
    ):
        self.physics = physics
        self.boost_amount = boost_amount
        self.jumped = jumped
        self.double_jumped = double_jumped


@dataclass(init=False, slots=True)
class BoostState:
    respawn_time: float | None

    def __init__(self, respawn_time: float | None = None):
        self.respawn_time = respawn_time


@dataclass(init=False, slots=True)
class GameInfoState:
    world_gravity_z: float | None
    game_speed: float | None
    paused: bool | None
    end_match: bool | None

    def __init__(
        self,
        world_gravity_z: float | None = None,
        game_speed: float | None = None,
        paused: bool | None = None,
        end_match: bool | None = None,
    ):
        self.world_gravity_z = world_gravity_z
        self.game_speed = game_speed
        self.paused = paused
        self.end_match = end_match


@dataclass(init=False, slots=True)
class GameState:
    ball: BallState | None
    cars: dict[int, CarState] | None
    boosts: list[BoostState] | None
    game_info: GameInfoState | None
    console_commands: list[str]

    def __init__(
        self,
        ball: BallState | None = None,
        cars: dict[int, CarState] | None = None,
        boosts: list[BoostState] | None = None,
        game_info: GameInfoState | None = None,
        console_commands: list[str] | None = None,
    ):
        self.ball = ball
        self.cars = cars
        self.boosts = boosts
        self.game_info = game_info
        self.console_commands = console_commands if console_commands else []
