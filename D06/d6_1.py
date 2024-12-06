from AoCInputHelper import fetch_input
from D06.Map import Map

input_data: str = fetch_input(2024, 6)
map = [line.strip() for line in input_data.split("\n")]

map_list: list[list[chr]] = [list(line) for line in map]
print(map_list)

current_map: Map = Map(map_list)
current_map = current_map.move()
current_map.print_map()

print(current_map.count_guarded_steps())
