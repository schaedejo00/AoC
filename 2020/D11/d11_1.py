import re
from copy import deepcopy

import numpy as np


def count_adjacent_occupied(seats, y, x):
    count = 0
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):

            if i == y and j == x or i < 0 or i >= len(seats) or j < 0 or j >= len(seats[y]):
                continue

            #print('y={}, x={}, leny={}, lenx={}'.format(y, x, len(seats), len(seats[y])))
            #print('seat[{}][{}]={}'.format(i, j, seats[i][j]))

            if seats[i][j] == '#':
                count += 1

    return count


def iterate_seats(seats):
    clone = deepcopy(seats)
    for i in range(0, len(seats)):
        for j in range(0, len(seats[i])):
            if seats[i][j] == '.':
                continue

            adjacent_occupied = count_adjacent_occupied(seats, i, j)

            if seats[i][j] == 'L' and adjacent_occupied == 0:
                clone[i][j] = '#'
            elif seats[i][j] == '#' and adjacent_occupied >= 4:
                clone[i][j] = 'L'
    return clone


def print_lines(lns):
    for l in lns:
        print("".join(l))
    #print(count_adjacent_occupied(lines, 5, 1))
    print()


with open('input.txt', 'r') as f:
    lines = f.read().split('\n')

for m in range(0, len(lines)):
    lines[m] = list(lines[m])

print_lines(lines)
last = []


while not last == lines:
    last = lines
    lines = iterate_seats(lines)
    print_lines(lines)

print(np.count_nonzero(np.array(lines) == '#'))
