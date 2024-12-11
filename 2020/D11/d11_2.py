import re
from copy import deepcopy
import numpy as np

def count_seen_occupied(seats, y, x):
    count = 0
    for i in range(- 1, 2):
        for j in range(- 1,  2):

            if i == 0 and j == 0 or y+i < 0 or y+i >= len(seats) or x+j < 0 or x+j >= len(seats[y]):
                continue

            #print('y={}, x={}, leny={}, lenx={}'.format(y, x, len(seats), len(seats[y])))
            #print('seat[{}][{}]={}'.format(i, j, seats[i][j]))

            if sees_occupied_in_direction(seats, y, x, i, j):
                count += 1

    return count

def sees_occupied_in_direction(seats, y, x, dirY, dirX):
    #print(seats[y][x])
    y = y + dirY
    x = x + dirX
    while y in range(0, len(seats)) and x in range(0, len(seats[0])):
        #print(seats[y][x], y, x)
        if seats[y][x] == '#':
            return True
        elif seats[y][x] == 'L':
            return False
        y = y + dirY
        x = x + dirX
    return False



def iterate_seats(seats):
    clone = deepcopy(seats)
    for i in range(0, len(seats)):
        for j in range(0, len(seats[i])):
            if seats[i][j] == '.':
                continue

            adjacent_occupied = count_seen_occupied(seats, i, j)

            if seats[i][j] == 'L' and adjacent_occupied == 0:
                clone[i][j] = '#'
            elif seats[i][j] == '#' and adjacent_occupied >= 5:
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

#print(count_seen_occupied(lines, 4, 3))


while not last == lines:
    last = lines
    lines = iterate_seats(lines)
    print_lines(lines)

print(np.count_nonzero(np.array(lines) == '#'))
