import sys
from queue import Queue

import numpy as np


class OctopusMap:
    map: list[list[int]]
    flashes: int = 0

    def __init__(self, map: list[list[int]]):
        self.map = map
        self.flashes = 0

    def __is_index_in_bounds(self, point: (int, int)) -> bool:
        x, y = point
        return 0 <= x < len(self.map) and 0 <= y < len(self.map[0])

    def simulate_flash(self):

        #increase all octupus by one
        self.map = [[octopus+1 for octopus in row] for row in self.map]
        print(self.map)

        #simulate flashes
        flashed: bool = True
        while flashed:
            flashed = False
            for x in range(0, len(self.map)):
                for y in range(0, len(self.map)):
                    if self.map[x][y] > 9:
                        self.map[x][y] = self.flash((x, y))
                        self.flashes += 1
                        flashed = True

        #set all flashed octopus 0 setzen
        self.map = [[0 if octopus < 0 else octopus for octopus in row ] for row in self.map]

    def simulate_flashes(self, amount: int = 1):
        for i in range(0, amount):
            self.simulate_flash()


    def simulate_flashes_until_synced(self) -> int:
        steps: int = 0
        while np.count_nonzero(self.map) > 0:
            self.simulate_flash()
            steps += 1
        return steps

    def flash(self, center: (int, int)) -> int:
        x, y = center

        for x_diff in [-1, 0, 1]:
            for y_diff in [-1, 0, 1]:
                if x_diff == y_diff == 0:
                    continue
                n_x = x + x_diff
                n_y = y + y_diff
                if self.__is_index_in_bounds((n_x, n_y)):
                    self.map[n_x][n_y] += 1
        # mark as flashed
        self.map[x][y] = -sys.maxsize - 1
        return self.map[x][y]
