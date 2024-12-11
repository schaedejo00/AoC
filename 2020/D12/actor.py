from operator import mod
from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270


class Actor:
    x = 0
    y = 0
    direction = 90

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def turn(self, degree, direction='R'):
        if direction == 'L':
            degree *= -1
        self.direction = mod(self.direction + degree, 360)

    def moveForward(self, steps):
        self.move(steps, Direction(self.direction))

    def move(self, steps, direction):
        if direction == Direction.NORTH or direction == 'N':
            self.y += -steps
        if direction == Direction.EAST or direction == 'E':
            self.x += steps
        if direction == Direction.SOUTH or direction == 'S':
            self.y += steps
        if direction == Direction.WEST or direction == 'W':
            self.x += -steps

    def manhattenDistanceTo(self,x,y):
        return abs(self.x - x)+abs(self.y - y)
