from app.action_field import ActionField
from app.figure.figure_abstract import FigureAbstract
from app.setting import Setting


class Collided:
    def figure_with_action_field_borders(self, figure: FigureAbstract) -> bool:
        for coordinate in figure.get_coordinates():
            if coordinate.get_x() == -1:
                return True

            if coordinate.get_x() > Setting.ACTION_FIELD_WIDTH - 1 or coordinate.get_y() > Setting.ACTION_FIELD_HEIGHT - 1:
                return True

        return False

    def figure_with_deactivate_figures(self, active_figure: FigureAbstract, deactivate_figures: list[FigureAbstract]):
        for deactivate_figure in deactivate_figures:
            for deactivate_coordinate in deactivate_figure.get_coordinates():
                for active_coordinate in active_figure.get_coordinates():
                    if active_coordinate == deactivate_coordinate:
                        return True
        return False
