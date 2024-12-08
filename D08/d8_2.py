from AoCInputHelper import get_grid, remove_entries_by_value, get_input, is_on_grid

# prepare input
input_data: dict[tuple[int, int], str]
input_data, nr, nc = get_grid(get_input(2024, 8))
data: dict[str, tuple[int, int]] = remove_entries_by_value(input_data, '.')
frequency_locations: dict[str, set[tuple[int, int]]] = dict()
for location, antenna in data.items():
    if frequency_locations.get(antenna) is None:
        frequency_locations[antenna] = set()
    frequency_locations[antenna].add(location)

# Find antinode locations
antinode_locations: set(tuple[int, int]) = set()
for frequency, locations in frequency_locations.items():
    print(f"Frequency {frequency} is broadcast from {len(locations)} locations")
    for location in locations:
        current_location: tuple[int, int] = location
        for interfering_location in locations:
            if current_location == interfering_location:
                continue
            antinode_locations.add(interfering_location)
            antinode_locations.add(current_location)

            delta: tuple[int, int] = (interfering_location[0] - current_location[0],
                                      interfering_location[1] - current_location[1])
            for j in range(1, max(nr, nc)):
                antinode_location = (
                    current_location[0] + j * delta[0],
                    current_location[1] + j * delta[1]
                )
                if is_on_grid(antinode_location, nr, nc):
                    antinode_locations.add(antinode_location)
                else:
                    break

print(f"There are {len(antinode_locations)} locations on the map containing antinodes")
