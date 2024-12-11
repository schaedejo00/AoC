from typing import List

import numpy as np


from D05.Point import Point

with open('example.txt', 'r', encoding="utf-8") as f:
#with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read()
fishes = [int(n) for n in puzzleInput.split(",")]

print("initial state", fishes)

for day in range(1, 256):
    newFishes = []
    for i in range(0, len(fishes)):
        fishes[i] -= 1
        if fishes[i] < 0:
            newFishes.append(8)
            fishes[i] = 6
    if len(newFishes) > 0:
        fishes = np.append(fishes, newFishes)
    #print("after", day, "days", fishes)

print(len(fishes))