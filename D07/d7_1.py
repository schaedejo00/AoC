from collections import deque
from typing import Deque

from AoCInputHelper import get_input


def solve(equation: Deque[int], tmp_results: Deque[int] = deque()) -> Deque[int]:
    if len(equation) == 0:
        return tmp_results
    if len(tmp_results) == 0:
        tmp_results.append(equation.popleft())
        return solve(equation, tmp_results)

    new_tmp_results: list[int] = []
    number: int = equation.popleft()
    while len(tmp_results) > 0:
        tmp: int = tmp_results.popleft()
        new_tmp_results.append(tmp + number)
        new_tmp_results.append(tmp * number)
    return solve(equation, deque(new_tmp_results))


input_data: str = get_input(2024, 7)
data: list[int, str] = [[int(l), [int(n) for n in r.strip().split(" ")]] for ln in input_data.split("\n")
                        for l, r in [ln.split(":", 1)]]

total: int = 0
for line in data:
    result, equation = line
    results: Deque[int] = solve(deque(equation))
    if result in results:
        total += result
print(total)
