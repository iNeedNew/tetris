from copy import deepcopy

from app.game_object.figure.figure_abstract import FigureAbstract
from app.game_object.freeze_figure_collection import FreezeFigureCollection


class FigureMoved:

    def __init__(self, pygame, collided):
        self.__pygame = pygame
        self.__collided = collided
        self.__layers = []

    def move(self, active_figure: FigureAbstract, freeze_figure_collection: FreezeFigureCollection):
        keys = self.__pygame.key.get_pressed()
        key_pressed = False
        copy_figure = deepcopy(active_figure)

        if keys[self.__pygame.K_LEFT]:
            copy_figure.add_position_horizontal(-1)
            key_pressed = True
        if keys[self.__pygame.K_RIGHT]:
            copy_figure.add_position_horizontal(1)
            key_pressed = True
        if keys[self.__pygame.K_DOWN]:
            copy_figure.add_position_vertical(1)
            key_pressed = True
        if keys[self.__pygame.K_UP]:
            copy_figure.rotate()
            key_pressed = True

        if key_pressed and not any([
            self.__collided.figure_with_action_field_borders(copy_figure),
            self.__collided.figure_with_freeze_figures(copy_figure, freeze_figure_collection)
        ]):
            active_figure.set_coordinates(copy_figure.get_coordinates()[:])
            active_figure.set_rotate(copy_figure.get_rotate())

    def fall(self, active_figure: FigureAbstract, freeze_figure_collection: FreezeFigureCollection) -> bool:

        self.__fall_freeze_figures(freeze_figure_collection)

        copy_figure = deepcopy(active_figure)
        copy_figure.add_position_vertical(1)

        if not any([
            self.__collided.figure_with_action_field_borders(copy_figure),
            self.__collided.figure_with_freeze_figures(copy_figure, freeze_figure_collection)
        ]):
            active_figure.add_position_vertical(1)
        else:
            freeze_figure_collection.add(active_figure)

            layers = freeze_figure_collection.find_filled_layers()

            if len(layers) > 0:
                self.__layers = layers
                freeze_figure_collection.remove_layers(layers)

            return True
        return False

    def __fall_freeze_figures(self, freeze_figure_collection: FreezeFigureCollection):
        pass

