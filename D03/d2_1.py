import re

sum: int = 0
pattern: str = r"mul\((?P<x>[1-9][0-9]*),(?P<y>[1-9][0-9]*)\)"


with open('input_1.txt', 'r') as f:
    while line := f.readline():
        for match in re.finditer(pattern, line):
            sum += int(match.group("x")) * int(match.group("y"))

print(sum)
