from app.game_object.figure.figure_abstract import FigureAbstract
from app.setting import Setting


class FreezeFigureCollection:
    def __init__(self):
        self.__collection: list[FigureAbstract] = []

    def add(self, figure: FigureAbstract):
        self.__collection.append(figure)

    def get(self) -> list[FigureAbstract]:
        return self.__collection

    def find_filled_layers(self):

        filled_layers = {}

        for figure in self.__collection:
            for coordinate in figure.get_coordinates():
                layer = coordinate.get_y()
                if layer in filled_layers:
                    filled_layers[layer] += 1
                else:
                    filled_layers[layer] = 1

        layers = []

        for layer in filled_layers:
            if filled_layers[layer] == Setting.ACTION_FIELD_WIDTH:
                layers.append(layer)

        return layers

    def remove_layers(self, layers):
        for figure in self.__collection:
            coordinates = figure.get_coordinates()
            for coordinate in coordinates[:]:
                if coordinate.get_y() in layers:
                    coordinates.remove(coordinate)

        for figure in self.__collection[:]:
            if len(figure.get_coordinates()) == 0:
                self.__collection.remove(figure)
