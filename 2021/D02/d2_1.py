from unittest import case

import numpy as np


with open('input_1.txt', 'r') as f:
    arr = np.genfromtxt(f, dtype=str, delimiter='\n')

horizontal = 0
depth = 0

for i in range(0, len(arr)):
    line = arr[i].split(" ")
    value = int(line[1])
    if(line[0] == "up"):
            depth -= value
    if (line[0] == "down"):
        depth += value
    if (line[0] == "forward"):
        horizontal += value

    print(line, depth, horizontal)

print (depth, horizontal, (depth*horizontal))


