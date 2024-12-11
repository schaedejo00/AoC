import re

def is_valid(update: list[int], order: dict[int, int]) -> bool:
    for i, current in enumerate(update):
        for j, before in enumerate(update[0:i]):
            if (current, before) in order:
                return False
    return True

pattern: str = r"(?P<before>[1-9][0-9]*)\|(?P<after>[1-9][0-9]*)"
order: list[(int, int)] = []
updates: list[list[int]] = []

with open('input_1.txt', 'r') as f:
    while line := f.readline():
        if match := re.match(pattern, line):
            order.append((int(match.group("before")), int(match.group("after"))))
        if "," in line:
            updates.append([int(x) for x in line.split(",")])

count: int = 0
for update in updates:
    if is_valid(update, order):
        count += update[int(len(update)/2)]

print (count)