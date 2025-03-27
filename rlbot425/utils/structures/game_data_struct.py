from dataclasses import dataclass
from enum import IntEnum
from typing import Sequence, TypeAlias

from rlbot import flat

Vector3: TypeAlias = flat.Vector3
Rotator: TypeAlias = flat.Rotator
Physics: TypeAlias = flat.Physics


@dataclass(frozen=True, slots=True)
class Touch:
    player_name: str
    time_seconds: float
    hit_location: Vector3
    hit_normal: Vector3
    team: int
    player_index: int


ScoreInfo: TypeAlias = flat.ScoreInfo
BoxShape: TypeAlias = flat.BoxShape
SphereShape: TypeAlias = flat.SphereShape
CylinderShape: TypeAlias = flat.CylinderShape


class ShapeType(IntEnum):
    box = 0
    sphere = 1
    cylinder = 2


@dataclass(frozen=True, slots=True)
class CollisionShape:
    type: ShapeType
    box: BoxShape
    sphere: SphereShape
    cylinder: CylinderShape


@dataclass(frozen=True, slots=True)
class PlayerInfo:
    physics: Physics
    score_info: ScoreInfo
    is_demolished: bool
    has_wheel_contact: bool
    is_super_sonic: bool
    is_bot: bool
    jumped: bool
    double_jumped: bool
    name: str
    team: int
    boost: int
    hitbox: BoxShape
    hitbox_offset: Vector3
    spawn_id: int


@dataclass(frozen=True, slots=True)
class BallInfo:
    physics: Physics
    latest_touch: Touch
    collision_shape: CollisionShape


BoostPadState: TypeAlias = flat.BoostPadState
TeamInfo: TypeAlias = flat.TeamInfo


@dataclass(frozen=True, slots=True)
class GameInfo:
    seconds_elapsed: float
    game_time_remaining: float
    is_overtime: bool
    is_unlimited_time: bool
    is_round_active: bool
    is_kickoff_pause: bool
    is_match_ended: bool
    world_gravity_z: float
    game_speed: float
    frame_num: int


@dataclass(frozen=True, slots=True)
class GameTickPacket:
    game_cars: Sequence[PlayerInfo]
    num_cars: int
    game_boosts: Sequence[BoostPadState]
    num_boost: int
    game_ball: BallInfo
    game_info: GameInfo
    teams: Sequence[TeamInfo]
    num_teams: int


BoostPad: TypeAlias = flat.BoostPad
GoalInfo: TypeAlias = flat.GoalInfo


@dataclass(frozen=True, slots=True)
class FieldInfoPacket:
    boost_pads: Sequence[BoostPad]
    num_boosts: int
    goals: Sequence[GoalInfo]
    num_goals: int
