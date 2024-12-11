
from OctopusMap import OctopusMap

#with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

octopusMap = OctopusMap([[int(n) for n in list(line)] for line in puzzleInput])

print(octopusMap.map)

octopusMap.simulate_flashes(100)

print(octopusMap.flashes)

