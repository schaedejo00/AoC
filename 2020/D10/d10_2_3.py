import re
from collections import defaultdict

import numpy as np


def generate_arrangements(nextAdapters):

    ways = defaultdict(int)
    ways[nextAdapters[0]] = 1
    print(ways)
    for i in range(1, len(nextAdapters)):
        ways[nextAdapters[i]] = ways[nextAdapters[i]-1] + ways[nextAdapters[i]-2] + ways[nextAdapters[i]-3]

    #print(nextAdapters[-1], ways[nextAdapters[-1]], ways)

    return ways[nextAdapters[-1]]


with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [int(x) for x in lines]
lines.append(0)
lines.sort()
lines.append(lines[-1] + 3)
print(lines)

res = generate_arrangements(lines)

print('count=', res)
