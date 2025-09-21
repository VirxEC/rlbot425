import json
import math
from threading import Thread

from rlbot import flat
from rlbot.managers import Bot

from rlbot425.agents.base_agent import BaseAgent
from rlbot425.matchconfig.match_config import MatchConfig
from rlbot425.messages.flat import QUICK_CHATS
from rlbot425.messages.flat.QuickChatSelection import QuickChatSelection
from rlbot425.utils.game_state_util import GameState
from rlbot425.utils.rendering.rendering_manager import RenderingManager
from rlbot425.utils.structures.ball_prediction_struct import BallPrediction
from rlbot425.utils.structures.game_data_struct import (
    BallInfo,
    BoxShape,
    CollisionShape,
    CylinderShape,
    FieldInfoPacket,
    GameInfo,
    GameTickPacket,
    PlayerInfo,
    ShapeType,
    SphereShape,
    Touch,
)


def v524_player_info(player: flat.PlayerInfo) -> PlayerInfo:
    return PlayerInfo(
        player.physics,
        player.score_info,
        player.demolished_timeout >= 0,
        player.air_state == flat.AirState.OnGround,
        player.is_supersonic,
        player.is_bot,
        player.has_jumped,
        player.has_double_jumped or player.has_dodged,
        player.name,
        player.team,
        round(player.boost),
        player.hitbox,
        player.hitbox_offset,
        player.player_id,
    )


def v524_touch(idx: int, player: flat.PlayerInfo) -> Touch:
    assert player.latest_touch is not None

    return Touch(
        player.name,
        player.latest_touch.game_seconds,
        player.latest_touch.location,
        player.latest_touch.normal,
        player.team,
        idx,
    )


def v524_shape(
    shape: flat.BoxShape | flat.SphereShape | flat.CylinderShape,
) -> CollisionShape:
    match shape:
        case flat.SphereShape():
            return CollisionShape(
                ShapeType.sphere,
                BoxShape(0, 0, 0),
                shape,
                CylinderShape(0, 0),
            )
        case flat.BoxShape():
            return CollisionShape(
                ShapeType.box,
                shape,
                SphereShape(0),
                CylinderShape(0, 0),
            )
        case flat.CylinderShape():
            return CollisionShape(
                ShapeType.cylinder,
                BoxShape(0, 0, 0),
                SphereShape(0),
                shape,
            )


def get_latest_touch(packet: flat.GamePacket) -> Touch:
    s = -math.inf
    touched_car = None
    for i, car in enumerate(packet.players):
        if not car.latest_touch or car.latest_touch.ball_index != 0:
            continue

        if touched_car is None or car.latest_touch.game_seconds > s:
            s = car.latest_touch.game_seconds
            touched_car = i, car

    return (
        Touch("", 0, flat.Vector3(), flat.Vector3(), 0, 0)
        if touched_car is None
        else v524_touch(touched_car[0], touched_car[1])
    )


def v524_ball_info(packet: flat.GamePacket, ball: flat.BallInfo) -> BallInfo:
    return BallInfo(
        ball.physics,
        get_latest_touch(packet),
        v524_shape(ball.shape),
    )


def v524_balls(packet: flat.GamePacket) -> BallInfo:
    return (
        v524_ball_info(packet, flat.BallInfo())
        if len(packet.balls) == 0
        else v524_ball_info(packet, packet.balls[0])
    )


def v524_game_info(match_info: flat.MatchInfo) -> GameInfo:
    return GameInfo(
        match_info.seconds_elapsed,
        match_info.game_time_remaining,
        match_info.is_overtime,
        match_info.is_unlimited_time,
        match_info.match_phase in {flat.MatchPhase.Kickoff, flat.MatchPhase.Active},
        match_info.match_phase == flat.MatchPhase.Kickoff,
        match_info.match_phase == flat.MatchPhase.Ended,
        match_info.world_gravity_z,
        match_info.game_speed,
        match_info.frame_num,
    )


def v524_packet(packet: flat.GamePacket) -> GameTickPacket:
    return GameTickPacket(
        [v524_player_info(player) for player in packet.players],
        len(packet.players),
        packet.boost_pads,
        len(packet.boost_pads),
        v524_balls(packet),
        v524_game_info(packet.match_info),
        packet.teams,
        len(packet.teams),
    )


def v524_field_info(field_info: flat.FieldInfo) -> FieldInfoPacket:
    return FieldInfoPacket(
        field_info.boost_pads,
        len(field_info.boost_pads),
        field_info.goals,
        len(field_info.goals),
    )


class BotRunner(Bot):
    child_class: type[BaseAgent]
    agent_instance: BaseAgent | None = None

    def send_from_queue(self):
        assert self.agent_instance is not None
        while 1:
            msg = self.agent_instance.matchcomms.outgoing_broadcast.get()
            if msg is None:
                break

            self.send_match_comm(
                bytes(json.dumps(msg), "utf-8"),
                None,
                False,
            )

    def __init__(
        self, child_class: type[BaseAgent], default_agent_id: str | None = None
    ):
        super().__init__(default_agent_id)
        self.child_class = child_class
        self.matchcomms_thread = Thread(target=self.send_from_queue, daemon=True)

    def initialize(self):
        self.agent_instance = self.child_class(self.name, self.team, self.index)
        self.agent_instance._field_info = v524_field_info(self.field_info)

        self.matchcomms_thread.start()

        self.agent_instance.renderer = RenderingManager(self.renderer)
        self.agent_instance.renderer.set_bot_index_and_team(self.index, self.team)

        self.agent_instance.send_quick_chat = self.send_quick_chat
        self.agent_instance.set_game_state = self.set_v4_game_state

        self.agent_instance.init_match_config(MatchConfig(self.match_config))
        self.agent_instance.initialize_agent()

    @staticmethod
    def handle_quick_chat(
        agent_instance: BaseAgent,
        index: int,
        team: int,
        display: str,
    ):
        quick_chat_idx = QUICK_CHATS.index(display)
        if quick_chat_idx == -1:
            return

        agent_instance.handle_quick_chat(
            index, team, QuickChatSelection(quick_chat_idx)
        )

    def handle_match_comm(
        self,
        index: int,
        team: int,
        content: bytes,
        display: str | None,
        team_only: bool,
    ):
        assert self.agent_instance is not None
        if display is not None and BotRunner.handle_quick_chat(
            self.agent_instance,
            index,
            team,
            display,
        ):
            # the message was a quick chat
            return

        # custom message
        # try to decode it assuming it's JSON
        try:
            msg_str = content.decode("utf-8")
            msg = json.loads(msg_str)
        except UnicodeDecodeError:
            return
        except json.JSONDecodeError:
            return

        # queue the incoming message to be handled by the agent
        self.agent_instance.matchcomms.incoming_broadcast.put(msg)

    def send_quick_chat(self, team_only: bool, quick_chat: QuickChatSelection):
        self.send_match_comm(
            bytes(),
            QUICK_CHATS[int(quick_chat)],
            team_only,
        )

    def set_v4_game_state(self, game_state: GameState):
        balls: dict[int, flat.DesiredBallState] = {}
        if game_state.ball:
            balls[0] = game_state.ball

        cars: dict[int, flat.DesiredCarState] = {}
        if game_state.cars:
            for key, car in game_state.cars.items():
                cars[key] = flat.DesiredCarState(
                    car.physics,
                    car.boost_amount,
                )

        match_info = None
        if game_state.game_info:
            match_info = flat.DesiredMatchInfo(
                game_state.game_info.world_gravity_z,
                game_state.game_info.game_speed,
            )

        self.set_game_state(balls, cars, match_info, game_state.console_commands)

    def get_output(self, packet: flat.GamePacket) -> flat.ControllerState:
        assert self.agent_instance is not None

        slices = self.ball_prediction.slices[::2]
        self.agent_instance._ball_prediction = BallPrediction(slices, len(slices))

        self.agent_instance.renderer.begin_rendering()
        controller = self.agent_instance.get_output(v524_packet(packet))
        self.agent_instance.renderer.end_rendering()

        return controller

    def retire(self):
        assert self.agent_instance is not None
        self.agent_instance.retire()
