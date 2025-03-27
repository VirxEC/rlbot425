from dataclasses import dataclass
from typing import Optional, TypeAlias

from rlbot import flat

Rotator: TypeAlias = flat.RotatorPartial
Vector3: TypeAlias = flat.Vector3Partial
Physics: TypeAlias = flat.DesiredPhysics
BallState: TypeAlias = flat.DesiredBallState


@dataclass(init=False, slots=True)
class CarState:
    physics: Optional[Physics]
    boost_amount: Optional[float]
    jumped: Optional[bool]
    double_jumped: Optional[bool]

    def __init__(
        self,
        physics: Optional[Physics] = None,
        boost_amount: Optional[float] = None,
        jumped: Optional[bool] = None,
        double_jumped: Optional[bool] = None,
    ):
        self.physics = physics
        self.boost_amount = boost_amount
        self.jumped = jumped
        self.double_jumped = double_jumped


@dataclass(init=False, slots=True)
class BoostState:
    def __init__(self, respawn_time: Optional[float] = None):
        self.respawn_time = respawn_time


@dataclass(init=False, slots=True)
class GameInfoState:
    def __init__(
        self,
        world_gravity_z: Optional[float] = None,
        game_speed: Optional[float] = None,
        paused: Optional[bool] = None,
        end_match: Optional[bool] = None,
    ):
        self.world_gravity_z = world_gravity_z
        self.game_speed = game_speed
        self.paused = paused
        self.end_match = end_match


@dataclass(init=False, slots=True)
class GameState:
    def __init__(
        self,
        ball: Optional[BallState] = None,
        cars: Optional[dict[int, CarState]] = None,
        boosts: Optional[list[BoostState]] = None,
        game_info: Optional[GameInfoState] = None,
        console_commands: list[str] = [],
    ):
        self.ball = ball
        self.cars = cars
        self.boosts = boosts
        self.game_info = game_info
        self.console_commands = console_commands
