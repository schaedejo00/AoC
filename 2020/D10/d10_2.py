import re
import numpy as np

#too slow, exponential growth

def generate_arrangements(currentState, nextAdapters, startIndex):
    #print('currentState={}, nextAdapters={}'.format(currentState, nextAdapters))
    #arrangements = [currentState]
    count = 0
    max = len(nextAdapters)

    for i in range(startIndex, max):
        last_value = currentState
        if (i+2) < max and nextAdapters[i + 2] - last_value <= 3:
            count += generate_arrangements(nextAdapters[i + 2], nextAdapters, i + 3)
        if (i+1) < max and nextAdapters[i + 1] - last_value <= 3:
            count += generate_arrangements(nextAdapters[i + 1], nextAdapters, i + 2)
        if nextAdapters[i] - last_value <= 3:
            currentState = nextAdapters[i]
        else:
            return 0
    count += 1
    return count


with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [int(x) for x in lines]
lines.sort()
print(lines)

res = generate_arrangements(0, lines, 0)

print('count=', res)
