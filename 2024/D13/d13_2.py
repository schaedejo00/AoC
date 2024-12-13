import sys
from typing import Iterator
import re

#second try
# prepare input
#input_data: str = get_input(2024, 13)
input_data: str = open('example.txt').read()


pattern_a: str = r"^Button A: X(?P<x_A>[+][1-9][0-9]*), Y(?P<y_A>[+][1-9][0-9]*)$"
pattern_b: str = r"^Button B: X(?P<x_B>[+][1-9][0-9]*), Y(?P<y_B>[+][1-9][0-9]*)$"
pattern_prize : str = r"^Prize: X=(?P<x_prize>[1-9][0-9]*), Y=(?P<y_prize>[1-9][0-9]*)$"
pattern: re.Pattern[str] = re.compile(pattern_a + "\n" + pattern_b + "\n" + pattern_prize, re.MULTILINE) #

matches: Iterator[re.Match] = pattern.finditer(input_data)
costs: list[int] = []
for match in matches:
    coordinates_a: tuple[int, int] = (int(match.group("x_A")[1:]), int(match.group("y_A")[1:]))
    coordinates_b: tuple[int, int] = (int(match.group("x_B")[1:]), int(match.group("y_B")[1:]))
    coorinates_prize: tuple[int, int] = (int(match.group("x_prize")) , int(match.group("y_prize")) )

    best: tuple[int, int] = (sys.maxsize, sys.maxsize)
    can_be_solved: bool = False
    cost: tuple[int, int] = (3, 1)

    #x_ges = x_a*n + x_b*m
    #m = x_prize/x_b
    #n = (x_prize - m*x_b)/x_a
    #
    m_start = int(coorinates_prize[0]/coordinates_b[0])
    m = m_start

    #iterate over all possible m values, starting from the highest possible value m_start
    for i in range(m_start, -1, -1):
        m = i
        n = int((coorinates_prize[0] - m * coordinates_b[0]) / coordinates_a[0])

        # x_ges = x_a*n + x_b*m and y_ges = y_a*n + y_b*m
        if n * coordinates_a[0] + m * coordinates_b[0] == coorinates_prize[0] and n * coordinates_a[1] + m * \
                coordinates_b[1] == coorinates_prize[1]:
            print(f"Solution found: A pressed {n} times, B pressed {m} times")
            print(f"Total cost: {n * 3 + m * 1}")
            candidate = (n, m)
            can_be_solved = True
            if (sum(x * y for x, y in zip(best, cost)) > sum(x * y for x, y in zip(candidate, cost))):
                best = candidate
    if can_be_solved:
        costs.append(sum(x * y for x, y in zip(best, cost)))

print(f"costs={costs}, sum={sum(costs)}")

