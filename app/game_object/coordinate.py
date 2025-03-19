class Coordinate:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def add_x(self, x: int) -> None:
        self.__x += x

    def get_y(self) -> int:
        return self.__y

    def add_y(self, y: int) -> None:
        self.__y += y

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.__x == other.__x and self.__y == other.__y
        return False

    def __repr__(self):
        return 'Coordinate({}, {})'.format(self.__x, self.__y)
