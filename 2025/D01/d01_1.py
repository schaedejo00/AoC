from collections import Counter, defaultdict
from operator import countOf
from typing import List, Tuple

from AoCInputHelper import get_input

#prepare input
input_data: List[Tuple[chr, int]] = [[x[0], int(x[1:])] for x in get_input(2025, 1).split('\n')]
#input_data: List[Tuple[chr, int]] = [[x[0], int(x[1:])] for x in open('example.txt').read().split('\n')]

dial_rotations: List[int] = [50]
count : int = 0
for rotation in input_data:
    count += rotation[1] // 100
    rotation[1] %= 100

    last_dial_rotation : int = dial_rotations[-1]

    if rotation[0] == 'L':
        new_dial_rotation = (last_dial_rotation - rotation[1])
    else:
        new_dial_rotation = (last_dial_rotation + rotation[1])

    if last_dial_rotation != 0 and (new_dial_rotation <= 0 or new_dial_rotation >= 100):
        count += 1

    dial_rotations.append(new_dial_rotation % 100)

print(count, input_data)
