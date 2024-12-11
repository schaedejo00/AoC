import numpy as np
import re

def count(grp):
    f = lambda x, y: x | y
    flags = np.zeros(letterCount, dtype=int)
    for i in range(0, len(grp)):
        for j in range(0, letterCount):
            flags[j] = f(flags[j], grp[i][j])

    print(flags)
    current = np.sum(flags)
    print('group={}, \n, flags={}, \n, current={}'.format(grp, flags, current))
    return current

with open('input.txt', 'r') as f:
    lines = f.readlines()
letterCount = 26
person = np.zeros(letterCount, dtype=int)
group = np.array([np.zeros(letterCount, dtype=int)])
sum = 0

for line in lines:

    if line[0] != '\n':
        for char in line:
            if char != '\n':
                i = ord(char) - ord('a')
                person[i]=1

        group = np.vstack([group, person])
        person = np.zeros(letterCount, dtype=int)
    else:

        sum += count(group)
        person = np.zeros(letterCount, dtype=int)
        group = np.array([np.zeros(letterCount, dtype=int)])

sum += count(group)
print(sum)
