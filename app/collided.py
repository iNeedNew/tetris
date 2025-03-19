from app.game_object.figure.figure_abstract import FigureAbstract
from app.game_object.freeze_figure_collection import FreezeFigureCollection
from app.setting import Setting


class Collided:
    def figure_with_action_field_borders(self, figure: FigureAbstract) -> bool:
        for coordinate in figure.get_coordinates():
            if coordinate.get_x() == -1:
                return True

            if coordinate.get_x() > Setting.ACTION_FIELD_WIDTH - 1 or coordinate.get_y() > Setting.ACTION_FIELD_HEIGHT - 1:
                return True

        return False

    def figure_with_freeze_figures(self, active_figure: FigureAbstract, freeze_figure_collection: FreezeFigureCollection):
        for freeze_figure in freeze_figure_collection.get():
            for freeze_coordinate in freeze_figure.get_coordinates():
                for active_coordinate in active_figure.get_coordinates():
                    if active_coordinate == freeze_coordinate:
                        return True
        return False
