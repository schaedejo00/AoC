from typing import List

import numpy as np


from D05.Point import Point

#with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read()
fishes = [int(n) for n in puzzleInput.split(",")]

print("initial state", fishes)
#count the amount fishes of each possible generation
brood = np.zeros(9, np.ulonglong)
for fish in fishes:
    brood[fish] += 1
print ("initial state", brood)

for day in range(1, 257):
    newBrood = np.zeros(9, np.ulonglong)

    #store new Fishes
    newBrood[8] = brood[0]

    #move all brood entries one day forward
    for i in range(1, len(brood)):
        newBrood[i-1] = brood[i]

    #add old fishes to slot 6
    newBrood[6] = newBrood[6] + newBrood[8]
    brood = newBrood
    print ("after", day, "days", brood)

print("fishcount", sum(brood))
