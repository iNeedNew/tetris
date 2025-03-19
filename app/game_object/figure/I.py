from app.game_object.coordinate import Coordinate
from app.game_object.figure.figure_abstract import FigureAbstract


class I(FigureAbstract):

    def _init_position(self) -> None:
        self._position_vertical = -3
        self._position_horizontal = 3

    def _init_coordinates(self):
        self._coordinates: list[Coordinate] = [
            Coordinate(0, 0),
            Coordinate(0, 1),
            Coordinate(0, 2),
            Coordinate(0, 3),
        ]

    def rotate(self):
        if self._rotate == 0:
            self._coordinates[0].add_x(1)
            self._coordinates[0].add_y(2)
            self._coordinates[1].add_y(1)
            self._coordinates[2].add_x(-1)
            self._coordinates[3].add_x(-2)
            self._coordinates[3].add_y(-1)
        elif self._rotate == 1:
            self._coordinates[0].add_x(-2)
            self._coordinates[0].add_y(1)
            self._coordinates[1].add_x(-1)
            self._coordinates[2].add_y(-1)
            self._coordinates[3].add_x(1)
            self._coordinates[3].add_y(-2)
        elif self._rotate == 2:
            self._coordinates[0].add_x(-1)
            self._coordinates[0].add_y(-2)
            self._coordinates[1].add_y(-1)
            self._coordinates[2].add_x(1)
            self._coordinates[3].add_x(2)
            self._coordinates[3].add_y(1)
        elif self._rotate == 3:
            self._coordinates[0].add_x(2)
            self._coordinates[0].add_y(-1)
            self._coordinates[1].add_x(1)
            self._coordinates[2].add_y(1)
            self._coordinates[3].add_x(-1)
            self._coordinates[3].add_y(2)
        self._add_rotate()
