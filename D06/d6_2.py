import copy
import numpy as np

from D06.Map import Map
from D06.Direction import Direction

def generate_possible_loop_maps(original_map: list[list[chr]]) -> list[Map]:
    base_map: list[list[chr]] = [row[:] for row in original_map]
    map_with_path: Map = Map([row[:] for row in base_map])
    start_x: int
    start_y: int
    direction: Direction
    start_x, start_y, direction = map_with_path.get_start()
    map_with_path.move()

    possible_loop_maps: list[Map] = []
    #Walls can only be placed along the path => rest can be ignored
    for y in range(map_with_path.get_height()):
        for x in range(map_with_path.get_width()):
            values: list[chr] = Direction.get_str_values()
            if map_with_path.get_value(x, y) in values:
                if not(x == start_x and y == start_y):
                    clone: list[list[chr]] = [row[:] for row in base_map]
                    clone[y][x] = "#"
                    cloned_map: Map = Map(clone)
                    possible_loop_maps.append(cloned_map)
                else:
                    print("Startpunkt", x, y)

    return possible_loop_maps
pattern: str = r"(^)"

with open('input_1.txt', 'r') as file:
    map = [line.strip() for line in file]

count: int = 0

map_list: list[list[chr]] = [list(line) for line in map]
maps: list[Map] = generate_possible_loop_maps(map_list)

print("Generated", len(maps), "maps")

for index, current_map in enumerate(maps):
    print("Map-Nr.", index)
    current_map = current_map.move()
    if current_map.has_loop():
        count += 1
        print(count, "Loops detected")

print(count)
