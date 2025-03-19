import sys
from time import time
from random import choice

from app.game_object.action_field import ActionField
from app.collided import Collided
from app.figure_moved import FigureMoved
from app.game_object.figure.figure_abstract import FigureAbstract
from app.game_object.freeze_figure_collection import FreezeFigureCollection
from app.render import Render
from app.setting import Setting
from app.game_object.figure import get_figures


class Game:
    def __init__(self):
        import pygame
        self.__pygame = pygame
        self.__screen = self.__pygame.display.set_mode((Setting.SCREEN_WIDTH, Setting.SCREEN_HEIGHT))

        self.__action_field: ActionField = ActionField()
        self.__freeze_figure_collection: FreezeFigureCollection = FreezeFigureCollection()
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
