from abc import ABC, abstractmethod
from copy import deepcopy

from app.game_object.coordinate import Coordinate


class FigureAbstract(ABC):

    def __init__(self, color: tuple[int, int, int]):

        self.color = color
        self._position_vertical: int = 0
        self._position_horizontal: int = 0

        self.__max_side_height: int = 0
        self.__max_side_width: int = 0

        self._rotate: int = 0
        self._center_rotate_coordinate_index: None | int = None
        self._coordinates: list[Coordinate] = []

        self._init_position()
        self._init_coordinates()
        self.add_position_vertical(self._position_vertical)
        self.add_position_horizontal(self._position_horizontal)

    @abstractmethod
    def _init_coordinates(self) -> None:
        pass

    @abstractmethod
    def _init_position(self) -> None:
        pass

    def __get_center(self) -> tuple[int, int]:

        if self._center_rotate_coordinate_index is not None:
            coordinate = self._coordinates[self._center_rotate_coordinate_index]
            return coordinate.get_x(), coordinate.get_y()

        min_x = min(coordinate.get_x() for coordinate in self._coordinates)
        max_x = max(coordinate.get_x() for coordinate in self._coordinates)
        min_y = min(coordinate.get_y() for coordinate in self._coordinates)
        max_y = max(coordinate.get_y() for coordinate in self._coordinates)

        center_x = (min_x + max_x) // 2
        center_y = (min_y + max_y) // 2

        return center_x, center_y

    def get_rotate(self) -> int:
        return self._rotate

    def set_rotate(self, rotate: int):
        self._rotate = rotate

    def _add_rotate(self):
        self._rotate += 1
        if self._rotate == 4:
            self._rotate = 0

    def get_coordinates(self) -> list[Coordinate]:
        return self._coordinates

    def set_coordinates(self, coordinates: list[Coordinate]):
        self._coordinates = coordinates

    def add_position_vertical(self, position_vertical):
        self._position_vertical += position_vertical
        for coordinate in self._coordinates:
            coordinate.add_y(position_vertical)

    def add_position_horizontal(self, position_horizontal):
        self._position_horizontal += position_horizontal
        for coordinate in self._coordinates:
            coordinate.add_x(position_horizontal)

    def remove_layer(self, layer: int):
        down_layer_coordinates = []
        up_layer_coordinates = []

        for coordinate in self._coordinates[:]:
            if layer == coordinate.get_y():
                pass
            elif layer > coordinate.get_y():
                down_layer_coordinates.append(coordinate)
            elif layer < coordinate.get_y():
                up_layer_coordinates.append(coordinate)
        figures = []
        if len(down_layer_coordinates) > 0:
            down_figure = deepcopy(self)
            down_figure.set_coordinates(down_layer_coordinates)
            figures.append(down_figure)

        if len(up_layer_coordinates) > 0:
            up_figure = deepcopy(self)
            up_figure.set_coordinates(up_layer_coordinates)
            figures.append(up_figure)
        del self

        return figures

    def rotate(self):
        center_x, center_y = self.__get_center()
        rotated_coordinates = []
        for coord_index, coord in enumerate(self._coordinates):
            shifted_x = coord.get_x() - center_x
            shifted_y = coord.get_y() - center_y

            new_x = -shifted_y
            new_y = shifted_x

            rotated_x = new_x + center_x
            rotated_y = new_y + center_y
            rotated_coordinates.append(Coordinate(rotated_x, rotated_y))
        self._coordinates = rotated_coordinates
        self._add_rotate()

    def __repr__(self):
        return '[{}]FigureSize({}x{})'.format(self.__class__.__name__, self.__max_side_width, self.__max_side_height)

    def layer_intersects(self, layer: int):
        for coordinate in self._coordinates:
            if coordinate.get_y() == layer:
                return True
        return False

    def split_by_layers(self, layers):

        for layer in layers:
            
            up_coordinates = []
            down_coordinates = []

            for coordinate in self._coordinates:
                if coordinate.get_y() == layer:
                    pass
                elif coordinate.get_y() > layer:
                    down_coordinates.append(coordinate)
                elif coordinate.get_y() < layer:
                    up_coordinates.append(coordinate)

