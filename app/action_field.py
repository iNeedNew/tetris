from app.coordinate import Coordinate
from app.setting import Setting


class ActionField:
    def __init__(self):
        self.__coordinates: list[Coordinate] = [Coordinate(x, y) for x in range(Setting.ACTION_FIELD_WIDTH) for y in
                                                range(Setting.ACTION_FIELD_HEIGHT)]

    def get_coordinates(self) -> list[Coordinate]:
        return self.__coordinates
