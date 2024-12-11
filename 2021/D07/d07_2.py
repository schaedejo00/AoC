from typing import List

import numpy as np

from D05.Point import Point

#with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read()
crabs = [int(n) for n in puzzleInput.split(",")]

print("initial state", crabs)
positionCost = np.zeros(np.max(crabs) + 1, int)
fuelCostsTmp = [int(i) for i in range(0, np.max(crabs) + 1)]
fuelCosts = [sum(fuelCostsTmp[0:i+1]) for i in range(0, len(fuelCostsTmp))]
print(fuelCosts)
for position in range(0, len(positionCost)):
    #abs(n - i) Anzahl Schritte
    #fuelCosts[abs(n - i)] Spritkosten um die Schritte auszuführen
    #=> Ergibt ein Array mit Spritkosten pro Crab um die gewünschte Position zu erreichen
    currentCost = [fuelCosts[abs(crab - position)] for crab in crabs]
    positionCost[position] = sum(currentCost)

print(min(positionCost), positionCost)
