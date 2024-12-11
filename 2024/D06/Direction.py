from enum import Enum


class Direction(Enum):
    NORTH = '^'
    EAST = '>'
    SOUTH = 'v'
    WEST = '<'

    def __next_x_y(self, x: int) -> int:
        diff: int = 0
        if self == Direction.EAST:
            diff = 1
        elif self == Direction.WEST:
            diff = -1
        return x + diff

    def __next_y(self, y: int) -> int:
        diff: int = 0
        if self == Direction.SOUTH:
            diff = 1
        elif self == Direction.NORTH:
            diff = -1
        return y + diff

    def next_coordinates(self, x: int, y: int) -> tuple[int, int]:
        return self.__next_x_y(x), self.__next_y(y)

    def next(self):
        cls = self.__class__
        members: list[Direction] = [e for e in Direction]
        index = (members.index(self) + 1) % len(members)
        return members[index]

    def previous(self):
        cls = self.__class__
        members: list[Direction] = [e for e in Direction]
        index = (members.index(self) - 1) % len(members)
        return members[index]

    @staticmethod
    def get_str_values() -> list[str]:
        return [e.value for e in Direction]