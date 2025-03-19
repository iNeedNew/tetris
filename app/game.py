import sys
from time import time
from random import choice

from app.game_object.action_field import ActionField
from app.collided import Collided
from app.figure_moved import FigureMoved
from app.game_object.coordinate import Coordinate
from app.game_object.figure.figure_abstract import FigureAbstract
from app.game_object.freeze_figure_collection import FreezeFigureCollection
from app.render import Render
from app.setting import Setting
from app.game_object.figure import get_figures, I


class Game:
    def __init__(self):
        import pygame
        self.__pygame = pygame
        self.__screen = self.__pygame.display.set_mode((Setting.SCREEN_WIDTH, Setting.SCREEN_HEIGHT))

        self.__action_field: ActionField = ActionField()
        self.__freeze_figure_collection: FreezeFigureCollection = FreezeFigureCollection()

        if Setting.DEBUG:
            figure_coordinates = [
                [Coordinate(0, 9), Coordinate(1, 9), Coordinate(2, 9), Coordinate(3, 9), Coordinate(4, 9), Coordinate(5, 9)],
                [Coordinate(0, 8), Coordinate(1, 8), Coordinate(2, 8), Coordinate(3, 8), Coordinate(4, 8), Coordinate(5, 8)],
                [Coordinate(0, 7), Coordinate(1, 7), Coordinate(2, 7), Coordinate(3, 7), Coordinate(4, 7), Coordinate(5, 7)],
                [Coordinate(0, 6), Coordinate(1, 6), Coordinate(2, 6), Coordinate(3, 6), Coordinate(4, 6), Coordinate(5, 6)],
                [Coordinate(0, 5), Coordinate(1, 5), Coordinate(2, 5), Coordinate(3, 5), Coordinate(4, 5), Coordinate(5, 5)],
                [Coordinate(0, 4), Coordinate(1, 4), Coordinate(2, 4), Coordinate(3, 4), Coordinate(4, 4)],
                [Coordinate(0, 3), Coordinate(1, 3), Coordinate(2, 3), Coordinate(3, 3), Coordinate(4, 3), Coordinate(5, 3)],
            ]
            for coordinates in figure_coordinates:
                obj = I((255, 255, 255))
                obj.set_coordinates(coordinates)
                self.__freeze_figure_collection.add(
                    obj
                )


        self.__active_figure: FigureAbstract = self.__generate_figure()

        self.__figure_moved: FigureMoved = FigureMoved(self.__pygame, Collided())
        self.__render: Render = Render(self.__pygame, self.__screen)

    def __generate_figure(self) -> FigureAbstract:
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

    def start(self):
        last_move_time = time()
        last_fall_time = time()
        while True:
            current_time = time()
            for event in self.__pygame.event.get():
                if event.type == self.__pygame.QUIT:
                    self.__pygame.quit()
                    sys.exit()

            if current_time - last_move_time >= 0.1:
                self.__figure_moved.move(self.__active_figure, self.__freeze_figure_collection)
                last_move_time = current_time

            if current_time - last_fall_time >= 1:
                if self.__figure_moved.fall(self.__active_figure, self.__freeze_figure_collection):
                    self.__active_figure = self.__generate_figure()

                last_fall_time = current_time

            self.__render.render(self.__active_figure, self.__freeze_figure_collection, self.__action_field)
