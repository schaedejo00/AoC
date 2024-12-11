import re

sum: int = 0
pattern: str = r"mul\((?P<x>[1-9][0-9]*),(?P<y>[1-9][0-9]*)\)|do\(\)|don\'t\(\)"
enabled: bool = True

with open('input_1.txt', 'r') as f:
    while line := f.readline():
        for match in re.finditer(pattern, line):
            if match.group() == "do()":
                enabled = True
            elif match.group() == "don't()":
                enabled = False
            elif enabled and match.group().startswith("mul"):
                sum += int(match.group("x")) * int(match.group("y"))

print(sum)
