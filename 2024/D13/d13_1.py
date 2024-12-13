from typing import Iterator

from AoCInputHelper import *
import re

#first try
# prepare input
input_data: str = get_input(2024, 13)
#input_data: str = open('example.txt').read()


pattern_a: str = r"^Button A: X(?P<x_A>[+][1-9][0-9]*), Y(?P<y_A>[+][1-9][0-9]*)$"
pattern_b: str = r"^Button B: X(?P<x_B>[+][1-9][0-9]*), Y(?P<y_B>[+][1-9][0-9]*)$"
pattern_prize : str = r"^Prize: X=(?P<x_prize>[1-9][0-9]*), Y=(?P<y_prize>[1-9][0-9]*)$"
pattern: re.Pattern[str] = re.compile(pattern_a + "\n" + pattern_b + "\n" + pattern_prize, re.MULTILINE) #

matches: Iterator[re.Match] = pattern.finditer(input_data)
costs: list[int] = []
for match in matches:
    coordinates_a: tuple[int, int] = (int(match.group("x_A")[1:]), int(match.group("y_A")[1:]))
    coordinates_b: tuple[int, int] = (int(match.group("x_B")[1:]), int(match.group("y_B")[1:]))
    coorinates_prize: tuple[int, int] = (int(match.group("x_prize")), int(match.group("y_prize")))

    best: tuple[int, int] = (100, 100)
    can_be_solved: bool = False
    cost: tuple[int, int] = (3, 1)
    for b in range(101):
        for a in range(101):
            if (coordinates_a[0] * a + coordinates_b[0] * b == coorinates_prize[0]
                    and coordinates_a[1] * a + coordinates_b[1] * b == coorinates_prize[1]):
                if sum(x*y for x, y in zip(best, cost)) > sum(x * y for x, y in zip((a, b), cost)):
                    best = (a, b)
                    can_be_solved = True
    if can_be_solved:
        costs.append(sum(x*y for x, y in zip(best, cost)))
        print(f"Solution found: A pressed {best[0]} times, B pressed {best[1]} times")
        print(f"Total cost: sum(x*y for x, y in zip(best, cost))")
    else:
        print("No solution found for this configuration")

print(f"costs={costs}, sum={sum(costs)}")

