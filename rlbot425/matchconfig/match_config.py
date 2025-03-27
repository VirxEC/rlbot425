from rlbot import flat

from rlbot425.parsing.match_settings_config_parser import (
    ball_bounciness_mutator_types,
    ball_max_speed_mutator_types,
    ball_size_mutator_types,
    ball_type_mutator_types,
    ball_weight_mutator_types,
    boost_amount_mutator_types,
    boost_strength_mutator_types,
    demolish_mutator_types,
    game_map_dict,
    game_mode_types,
    game_speed_mutator_types,
    gravity_mutator_types,
    match_length_types,
    max_score_types,
    overtime_mutator_types,
    respawn_time_mutator_types,
    rumble_mutator_types,
    series_length_mutator_types,
)


class MutatorConfig:
    """
    Represent mutator configuration, e.g. match length, boost amount, etc.

    Knows how to translate itself into the MutatorSettings ctypes class.
    """

    def __init__(self, mutators: flat.MutatorSettings):
        self.match_length = match_length_types[int(mutators.match_length)]
        self.max_score = max_score_types[int(mutators.max_score)]
        self.overtime = overtime_mutator_types[int(mutators.overtime)]
        self.series_length = series_length_mutator_types[int(mutators.series_length)]
        self.game_speed = game_speed_mutator_types[int(mutators.game_speed)]
        self.ball_max_speed = ball_max_speed_mutator_types[int(mutators.ball_max_speed)]
        self.ball_type = ball_type_mutator_types[int(mutators.ball_type)]
        self.ball_weight = ball_weight_mutator_types[int(mutators.ball_weight)]
        self.ball_size = ball_size_mutator_types[int(mutators.ball_size)]
        self.ball_bounciness = ball_bounciness_mutator_types[
            int(mutators.ball_bounciness)
        ]
        self.boost_amount = boost_amount_mutator_types[int(mutators.boost_amount)]
        self.rumble = rumble_mutator_types[int(mutators.rumble)]
        self.boost_strength = boost_strength_mutator_types[int(mutators.boost_strength)]
        self.gravity = gravity_mutator_types[int(mutators.gravity)]
        self.demolish = demolish_mutator_types[int(mutators.demolish)]
        self.respawn_time = respawn_time_mutator_types[int(mutators.respawn_time)]


class MatchConfig:
    """
    Represents configuration for an entire match. Includes player config and mutators.
    """

    def __init__(self, match_config: flat.MatchConfiguration):
        self.game_mode = game_mode_types[int(match_config.game_mode)]

        self.game_map: str = ""
        for key, value in game_map_dict.items():
            if value == match_config.game_map_upk:
                self.game_map = key
                break

        self.mutators: MutatorConfig = (
            MutatorConfig(flat.MutatorSettings())
            if match_config.mutators is None
            else MutatorConfig(match_config.mutators)
        )
