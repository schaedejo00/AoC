from unittest import case

import numpy as np
import re

with open('input_1.txt', 'r') as f:
#with open('example.txt', 'r') as f:
    arr = np.genfromtxt(f, dtype=str, delimiter='\n')

horizontal = 0
depth = 0
aim = 0

for i in range(0, len(arr)):
    line = arr[i].split(" ")
    value = int(line[1])
    if(line[0] == "up"):
        aim -= value
    if (line[0] == "down"):
        aim += value
    if (line[0] == "forward"):
        horizontal += value
        depth = depth + value * aim

    print(line, depth, horizontal, aim)

print (depth, horizontal, (depth*horizontal))


