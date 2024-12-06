import re
import numpy as np
from D06.Map import Map


pattern: str = r"(^)"
map: np.ndarray = np.genfromtxt("example.txt", delimiter="\n", dtype=str)

with open('input_1.txt', 'r') as file:
    map = [line.strip() for line in file]

map_list: list[list[chr]] = [list(line) for line in map]
print(map_list)

current_map: Map = Map(map_list)

current_map = current_map.move()



current_map.print_map()

print(current_map.count_guarded_steps())