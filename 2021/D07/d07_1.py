from typing import List

import numpy as np


from D05.Point import Point

#with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read()
crabs = [int(n) for n in puzzleInput.split(",")]

print("initial state", crabs)
positionCost = np.zeros(np.max(crabs) + 1, int)

for i in range(0, len(positionCost)):
    positionCost[i] = sum([abs(n-i) for n in crabs])

print(min(positionCost), positionCost)