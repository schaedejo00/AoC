from queue import Queue

import numpy as np


class Map:
    map: list[list[int]]

    def __init__(self, map: list[list[int]]):
        self.map = map

    def is_low_point(self, point: (int, int)) -> bool:
        x, y = point
        value = self.map[x][y]
        neighbours = self.get_neighbours_of_point((x, y))
        for neighbour in neighbours:
            nX, nY = neighbour
            if value >= self.map[nX][nY]:
                return False
        return True

    def get_lowpoints(self) -> list[(int, int)]:
        result = []
        for x in range(0, len(self.map)):
            for y in range(0, len(self.map[1])):
                if self.is_low_point((x, y)):
                    result.append((x, y))
        return result

    def __is_index_in_bounds(self, point: (int, int)) -> bool:
        x, y = point
        return 0 <= x < len(self.map) and 0 <= y < len(self.map[0])


    def compute_basin_size(self, point: (int, int)) -> int:
        neighbours = Queue()
        [neighbours.put(n) for n in self.get_neighbours_of_point(point)]

        checked: list[(int, int)] = [point]
        basin: list[(int, int)] = [point]
        while not neighbours.empty():
            neighbour = neighbours.get()
            x, y = neighbour
            if neighbour not in checked and self.map[x][y] < 9:
                basin.append(neighbour)
                [neighbours.put(n) for n in self.get_neighbours_of_point(neighbour) if n not in checked]
            checked.append(neighbour)
        # print("basin", point, basin)
        return len(basin)

    def get_neighbours_of_point(self, point: (int, int)) -> list[(int, int)]:
        xDiff: [int] = [-1, 0, 0, 1]
        yDiff: [int] = [0, -1, 1, 0]
        x, y = point
        neighbours: [(int, int)] = []
        for i in range(0, len(xDiff)):
            xToCheck: int = x + xDiff[i]
            yToCheck: int = y + yDiff[i]
            if self.__is_index_in_bounds((xToCheck, yToCheck)):
                neighbours.append((xToCheck, yToCheck))
        return neighbours
