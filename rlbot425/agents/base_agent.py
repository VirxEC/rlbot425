from typing import TypeAlias

from rlbot import flat

from rlbot425.matchconfig.match_config import MatchConfig
from rlbot425.messages.flat.QuickChatSelection import QuickChatSelection
from rlbot425.utils.game_state_util import GameState
from rlbot425.utils.rendering.rendering_manager import RenderingManager
from rlbot425.utils.structures.ball_prediction_struct import BallPrediction
from rlbot425.utils.structures.game_data_struct import FieldInfoPacket, GameTickPacket

SimpleControllerState: TypeAlias = flat.ControllerState


class BaseAgent:
    name: str
    team: int
    index: int

    renderer: RenderingManager

    _field_info: FieldInfoPacket = FieldInfoPacket([], 0, [], 0)
    _ball_prediction: BallPrediction = BallPrediction([], 0)

    def __init__(self, name: str, team: int, index: int):
        self.name = name
        self.team = team
        self.index = index

    def initialize_agent(self):
        """
        Called for all heaver initialization that needs to happen.
        The config is fully loaded at this point
        """
        pass

    def init_match_config(self, match_config: MatchConfig):
        """
        Override this method if you would like to be informed of what config was used to start the match.
        Useful for knowing what map you're on, mutators, etc.
        """

    def get_field_info(self) -> FieldInfoPacket:
        """
        Gets the information about the field.
        This does not change during a match so it only needs to be called once after the everything is loaded.
        """
        return self._field_info

    def get_ball_prediction_struct(self) -> BallPrediction:
        """Fetches a prediction of where the ball will go during the next few seconds."""
        return self._ball_prediction

    def set_game_state(self, game_state: GameState):
        """CHEAT: Change the rocket league game to the given game_state"""

    def handle_quick_chat(self, index: int, team: int, quick_chat: QuickChatSelection):
        """
        Handles a quick chat from another bot.
        This will not receive any chats that this bot sends out.
        Currently does nothing, override to add functionality.

        :param index: Returns the index in the list of game cars that sent the quick chat
        :param team: Which team this player is on
        :param quick_chat: What the quick chat selection was
        """

    def send_quick_chat(self, team_only, quick_chat):
        """
        Sends a quick chat to the other bots.
        If it is QuickChats.CHAT_NONE or None it does not send a quick chat to other bots.

        :param team_only: either True or False, this says if the quick chat should only go to team members.
        :param quick_chat: The quick chat selection, available chats are defined in quick_chats.py
        """

    def get_output(self, game_tick_packet: GameTickPacket) -> SimpleControllerState:
        """
        Where all the logic of your bot gets its input and returns its output.

        :param game_tick_packet: see https://github.com/RLBot/RLBotPythonExample/wiki/Input-and-Output-Data
        :return: [throttle, steer, pitch, yaw, roll, jump, boost, handbrake]
        """
        raise NotImplementedError("get_output() must be implemented in the subclass")

    def retire(self):
        """
        Called after the game ends
        """
