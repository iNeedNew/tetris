from app.game_object.action_field import ActionField
from app.game_object.freeze_figure_collection import FreezeFigureCollection
from app.setting import Setting


class Render:
    def __init__(self, pygame, screen):
        self.__pygame = pygame
        self.__screen = screen

    def render(self, active_figure, freeze_figure_collection: FreezeFigureCollection, action_field: ActionField):

        for action_field_coordinate in action_field.get_coordinates():
            rect = (
                action_field_coordinate.get_x() * Setting.GUI_SCALE,
                action_field_coordinate.get_y() * Setting.GUI_SCALE,
                Setting.GUI_SCALE, Setting.GUI_SCALE
            )
            self.__pygame.draw.rect(self.__screen, (10, 10, 10), rect, 5)

        for coordinate in active_figure.get_coordinates():
            rect = (
                coordinate.get_x() * Setting.GUI_SCALE, coordinate.get_y() * Setting.GUI_SCALE,
                Setting.GUI_SCALE, Setting.GUI_SCALE
            )
            self.__pygame.draw.rect(self.__screen, active_figure.color, rect, 5)

        for figure in freeze_figure_collection.get():
            for coordinate in figure.get_coordinates():
                rect = (
                    coordinate.get_x() * Setting.GUI_SCALE, coordinate.get_y() * Setting.GUI_SCALE,
                    Setting.GUI_SCALE, Setting.GUI_SCALE
                )
                self.__pygame.draw.rect(self.__screen, self.__transform_freeze_figure_color(figure.color), rect, 5)

        self.__pygame.display.update()

    def __transform_freeze_figure_color(self, color: tuple[int, int, int]):
        new_color = []
        for scale in color:
            if scale > 100:
                new_color.append(100)
            else:
                new_color.append(0)
        return new_color[0], new_color[1], new_color[2]