from typing import List

import numpy as np


from D05.Point import Point

#with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    # arr = np.genfromtxt(f, dtype=str, delimiter='\n')
    puzzleInput = f.read()
puzzleInput = puzzleInput.replace(" -> ", ",")
ventLines = [[int(n) for n in line.strip().split(",")] for line in puzzleInput.split("\n")]
maxDim = np.amax(ventLines)+1
oceanFloor = np.zeros((maxDim, maxDim), int)
print(ventLines)

for line in ventLines:
    start:Point = Point(line[0], line[1])
    end:Point = Point(line[2], line[3])
    #print (start, end)
    linePoints = start.getAllPointsTo(end)
    #print ([(point.x, point.y) for point in linePoints])
    for point in linePoints:
        oceanFloor[point.x][point.y] += 1

print(oceanFloor)
overlap = [n for n in oceanFloor.flatten() if n > 1]
print(overlap, len(overlap))
