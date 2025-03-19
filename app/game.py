from app.action_field import ActionField
from app.collided import Collided
from app.figure.figure_abstract import FigureAbstract
from app.setting import Setting
import sys
from time import time
from copy import deepcopy
from app.figure import get_figures
from random import choice


class Game:
    def __init__(self):
        self.__init_gui()
        self.__init_objects()

        self.__collided = Collided()

    def __init_gui(self):
        import pygame
        self.__pygame = pygame
        self.__screen = self.__pygame.display.set_mode((Setting.SCREEN_WIDTH, Setting.SCREEN_HEIGHT))

    def __init_objects(self):
        self.__action_field: ActionField = ActionField()
        self.__deactivate_figures: list[FigureAbstract] = []
        self.__active_figure = self.__generate_figure()
        print(self.__active_figure)

    def __generate_figure(self):
        return choice(get_figures())(
            choice([
                (255, 0, 0),
                (0, 255, 0),
                (0, 0, 255),

                (255, 255, 0),
                (255, 0, 255),
                (0, 255, 255),
            ])
        )

    def __render(self):

        for action_field_coordinate in self.__action_field.get_coordinates():
            rect = (
                action_field_coordinate.get_x() * Setting.GUI_SCALE,
                action_field_coordinate.get_y() * Setting.GUI_SCALE,
                Setting.GUI_SCALE, Setting.GUI_SCALE
            )
            self.__pygame.draw.rect(self.__screen, (10, 10, 10), rect, 5)

        for coordinate in self.__active_figure.get_coordinates():
            rect = (
                coordinate.get_x() * Setting.GUI_SCALE, coordinate.get_y() * Setting.GUI_SCALE,
                Setting.GUI_SCALE, Setting.GUI_SCALE
            )
            self.__pygame.draw.rect(self.__screen, self.__active_figure.color, rect, 5)

        for figure in self.__deactivate_figures:
            for coordinate in figure.get_coordinates():
                rect = (
                    coordinate.get_x() * Setting.GUI_SCALE, coordinate.get_y() * Setting.GUI_SCALE,
                    Setting.GUI_SCALE, Setting.GUI_SCALE
                )
                self.__pygame.draw.rect(self.__screen, self.__transform_deactivate_figure_color(figure.color), rect, 5)

        self.__pygame.display.update()

    def __transform_deactivate_figure_color(self, color: tuple[int, int, int]):
        deactivate_color = []
        for scale in color:
            if scale > 100:
                deactivate_color.append(100)
            else:
                deactivate_color.append(0)
        return deactivate_color[0], deactivate_color[1], deactivate_color[2]

    def __move(self, keys):
        key_pressed = False
        new_figure = deepcopy(self.__active_figure)

        if keys[self.__pygame.K_LEFT]:
            new_figure.add_position_horizontal(-1)
            key_pressed = True
        if keys[self.__pygame.K_RIGHT]:
            new_figure.add_position_horizontal(1)
            key_pressed = True
        if keys[self.__pygame.K_DOWN]:
            new_figure.add_position_vertical(1)
            key_pressed = True
        if keys[self.__pygame.K_UP]:
            new_figure.rotate()
            key_pressed = True

        if key_pressed and not any([
            self.__collided.figure_with_action_field_borders(new_figure),
            self.__collided.figure_with_deactivate_figures(new_figure, self.__deactivate_figures)
        ]):
            self.__active_figure.set_coordinates(new_figure.get_coordinates()[:])
            self.__active_figure.set_rotate(new_figure.get_rotate())

    def __fall(self):
        new_figure = deepcopy(self.__active_figure)
        new_figure.add_position_vertical(1)

        if not any([
            self.__collided.figure_with_action_field_borders(new_figure),
            self.__collided.figure_with_deactivate_figures(new_figure, self.__deactivate_figures)
        ]):
            self.__active_figure.add_position_vertical(1)
        else:
            self.__deactivate_figures.append(self.__active_figure)
            self.__active_figure = self.__generate_figure()


    def __find_filled_layers(self) -> list[int]:

        filled_layers = {}

        for figure in self.__deactivate_figures:
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

    def start(self):
        last_move_time = time()
        last_fall_time = time()
        while True:
            current_time = time()
            for event in self.__pygame.event.get():
                if event.type == self.__pygame.QUIT:
                    self.__pygame.quit()
                    sys.exit()

            keys = self.__pygame.key.get_pressed()

            if current_time - last_move_time >= 0.1:
                self.__move(keys)
                last_move_time = current_time

            if current_time - last_fall_time >= 1:
                self.__fall()
                last_fall_time = current_time

            self.__render()
