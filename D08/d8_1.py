from AoCInputHelper import get_grid, remove_entries_by_value, get_input, is_on_grid

# prepare input
input_data: dict[tuple[int, int], str]
input_data, nr, nc = get_grid(get_input(2024, 8))
data: dict[str, tuple[int, int]] = remove_entries_by_value(input_data, '.')
frequency_locations: dict[str, set[tuple[int, int]]] = dict()
for location, frequency in data.items():
    if frequency_locations.get(frequency) is None:
        frequency_locations[frequency] = set()
    frequency_locations[frequency].add(location)

#
antinode_locations: set(tuple[int, int]) = set()
for frequency, locations in frequency_locations.items():
    print(f"Frequency {frequency} is broadcast from {len(locations)} locations")
    for location in locations:
        current_location: tuple[int, int] = location
        for interfering_location in locations:
            if current_location == interfering_location:
                continue
            delta: tuple[int, int] = (interfering_location[0] - current_location[0],
                                      interfering_location[1] - current_location[1])
            antinode_location = (
                current_location[0] + 2 * delta[0],
                current_location[1] + 2 * delta[1]
            )
            if is_on_grid(antinode_location, nr, nc):
                antinode_locations.add(antinode_location)

print(f"There are {len(antinode_locations)} locations on the map containing antinodes")
