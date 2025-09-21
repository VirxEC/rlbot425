from typing import TypeAlias

from rlbot import flat
from rlbot.managers import Renderer

Color: TypeAlias = flat.Color

MAX_INT = 2147483647 // 2
DEFAULT_GROUP_ID = "default"


class RenderingManager:
    bot_index: int = 0
    bot_team: int = 0

    def __init__(self, renderer: Renderer):
        self._renderer: Renderer = renderer

    def set_bot_index_and_team(self, bot_index: int = 0, bot_team: int = 0):
        self.bot_index = bot_index
        self.bot_team = bot_team

    def begin_rendering(self, group_id: str = DEFAULT_GROUP_ID):
        self._renderer.begin_rendering(group_id)

    def end_rendering(self):
        self._renderer.end_rendering()

    def clear_screen(self):
        self._renderer.clear_render_group(DEFAULT_GROUP_ID)

    def clear_all_touched_render_groups(self):
        """
        Clears all render groups which have been drawn to using `begin_rendering(group_id)`.
        Note: This does not clear render groups created by e.g. other bots.
        """
        self._renderer.clear_all_render_groups()

    def is_rendering(self):
        return self._renderer.is_rendering()

    def draw_line_3d(self, vec1, vec2, color: Color):
        self._renderer.draw_line_3d(
            self.__create_vector(vec1),
            self.__create_vector(vec2),
            color,
        )
        return self

    def draw_polyline_3d(self, vectors: list, color: Color):
        self._renderer.draw_polyline_3d(
            [self.__create_vector(vec) for vec in vectors], color
        )
        return self

    def draw_rect_2d(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        filled: bool,
        color: Color,
    ):
        self._renderer.draw_rect_2d(
            x / 1920, y / 1080, width / 1920, height / 1080, color
        )
        return self

    def draw_rect_3d(
        self,
        vec,
        width: float,
        height: float,
        filled: bool,
        color: Color,
        centered: bool = False,
    ):
        if centered:
            halign = flat.TextHAlign.Center
            valign = flat.TextVAlign.Center
        else:
            halign = flat.TextHAlign.Left
            valign = flat.TextVAlign.Top

        self._renderer.draw_rect_3d(
            self.__create_vector(vec),
            width / 1920,
            height / 1080,
            color,
            halign,
            valign,
        )
        return self

    def draw_string_2d(
        self,
        x: float,
        y: float,
        scale_x: float,
        scale_y: float,
        text: str,
        color: Color,
    ):
        self._renderer.draw_string_2d(text, x / 1920, y / 1080, scale_x, color)
        return self

    def draw_string_3d(
        self, vec, scale_x: float, scale_y: float, text: str, color: Color
    ):
        self._renderer.draw_string_3d(text, self.__create_vector(vec), scale_x, color)
        return self

    def create_color(self, alpha: int, red: int, green: int, blue: int) -> Color:
        return Color(red, green, blue, alpha)

    def black(self):
        return self.create_color(255, 0, 0, 0)

    def white(self):
        return self.create_color(255, 255, 255, 255)

    def gray(self):
        return self.create_color(255, 128, 128, 128)

    def grey(self):
        return self.gray()

    def blue(self):
        return self.create_color(255, 0, 0, 255)

    def red(self):
        return self.create_color(255, 255, 0, 0)

    def green(self):
        return self.create_color(255, 0, 128, 0)

    def lime(self):
        return self.create_color(255, 0, 255, 0)

    def yellow(self):
        return self.create_color(255, 255, 255, 0)

    def orange(self):
        return self.create_color(255, 225, 128, 0)

    def cyan(self):
        return self.create_color(255, 0, 255, 255)

    def pink(self):
        return self.create_color(255, 255, 0, 255)

    def purple(self):
        return self.create_color(255, 128, 0, 128)

    def teal(self):
        return self.create_color(255, 0, 128, 128)

    def team_color(self, team=None, alt_color=False):
        """
        Returns the team color of the bot. Team 0: blue, team 1: orange, other: white

        :param team: Specify which team's color. If None, the associated bot's team color will be returned.
        :param alt_color: If True, returns the alternate team colors instead. Team 0: cyan, team 1: red, other: gray
        :return: a team color
        """
        if team is None:
            team = self.bot_team

        if team == 0:
            return self.cyan() if alt_color else self.blue()
        elif team == 1:
            return self.red() if alt_color else self.orange()
        else:
            return self.gray() if alt_color else self.white()

    def __create_vector(self, *vec) -> flat.Vector3:
        """
        Converts a variety of vector types to a flatbuffer Vector3.
        Supports Flatbuffers Vector3, cTypes Vector3, list/tuple of numbers, or passing x,y,z (z optional)
        """
        import numbers

        if len(vec) == 1:
            if hasattr(vec[0], "__getitem__"):  # Support all subscriptable types.
                try:
                    x = float(vec[0][0])
                    y = float(vec[0][1])
                    try:
                        z = float(vec[0][2])
                    except (ValueError, IndexError):
                        z = 0
                except ValueError:
                    raise ValueError(
                        f"Unexpected type(s) for creating vector: {type(vec[0][0])}, {type(vec[0][1])}"
                    )
                except IndexError:
                    raise IndexError(
                        f"Unexpected IndexError when creating vector from type: {type(vec[0])}"
                    )
            elif isinstance(vec[0], flat.Vector3):
                x = vec[0].x
                y = vec[0].y
                z = vec[0].z
            else:
                raise ValueError(f"Unexpected type for creating vector: {type(vec[0])}")
        elif len(vec) == 2 or len(vec) == 3:
            if isinstance(vec[0], numbers.Number) and isinstance(
                vec[1], numbers.Number
            ):
                x = vec[0]
                y = vec[1]
                if len(vec) == 2:
                    z = 0
                else:
                    if isinstance(vec[2], numbers.Number):
                        z = vec[2]
                    else:
                        raise ValueError(
                            f"Unexpected type for creating vector: {type(vec[0])}"
                        )
            else:
                raise ValueError(
                    f"Unexpected type(s) for creating vector: {type(vec[0])}, {type(vec[1])}"
                )
        else:
            raise ValueError("Unexpected number of arguments for creating vector")

        return flat.Vector3(x, y, z)
