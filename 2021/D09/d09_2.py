from math import prod

from Map import Map

#with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

heightMap = Map([[int(n) for n in list(line)] for line in puzzleInput])

print(heightMap.map)

lowPoints = heightMap.get_lowpoints()

basins: list[int] = []
for point in lowPoints:
    basinSize = heightMap.compute_basin_size(point)
    basins.append(basinSize)
    print(point, basinSize)
basins.sort(reverse=True)
print(basins[0:3], prod(basins[0:3]))
