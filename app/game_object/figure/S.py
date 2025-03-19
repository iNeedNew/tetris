from app.game_object.coordinate import Coordinate
from app.game_object.figure.figure_abstract import FigureAbstract


class S(FigureAbstract):

    def _init_position(self) -> None:
        self._position_vertical = -3
        self._position_horizontal = 0

    def _init_coordinates(self):
        self._coordinates: list[Coordinate] = [
            Coordinate(1, 0), Coordinate(2, 0),
            Coordinate(0, 1), Coordinate(1, 1),
        ]
        self._center_rotate_coordinate_index = 1

