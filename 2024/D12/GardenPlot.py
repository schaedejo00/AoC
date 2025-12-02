import numpy as np


class GardenPlot:

    def __init__(self, position:tuple[int, int]):
        self.position = position
        self.fences:list[int] = [True, True, True, True] # N, E, S, W

    def remove_fence(self, direction):
        self.fences[direction] = False
