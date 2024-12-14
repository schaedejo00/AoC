
import re

from AoCInputHelper import *

# prepare input
input_data: list[str] = get_input(2024, 14).split("\n")
#input_data: list[str] = open('example.txt').read().split("\n")

pattern: str = r"p=(?P<p_x>-?\d+),(?P<p_y>-?\d+) v=(?P<v_x>-?\d+),(?P<v_y>-?\d+)"
pattern: re.Pattern[str] = re.compile(pattern)
max_x: int = 101
max_y: int = 103
seconds: int = 100

robots: list[tuple[int, int, int, int]] = []
for line in input_data:
    match: re.Match = pattern.match(line)
    robot: tuple[int, int, int, int] = (int(match.group("p_x")), int(match.group("p_y")), int(match.group("v_x")), int(match.group("v_y")))
    robots.append(robot)
    print(f"Robot at {robot[0], robot[1]} moving with {robot[2], robot[3]}")

quadrants: list[int] = [0, 0, 0, 0]
for i, robot in enumerate(robots):
    for j in range(seconds):
        robot = ((robot[0] + robot[2])%max_x, (robot[1] + robot[3])%max_y, robot[2], robot[3])
    robots[i] = robot
    print(f"Robot at {robot[0], robot[1]} moving with {robot[2], robot[3]}")
    if (robot[0] < max_x//2 and robot[1] < max_y//2):
        quadrants[0] += 1
    elif (robot[0] > max_x//2 and robot[1] < max_y//2):
        quadrants[1] += 1
    elif (robot[0] < max_x//2 and robot[1] > max_y//2):
        quadrants[2] += 1
    elif (robot[0] > max_x//2 and robot[1] > max_y//2):
        quadrants[3] += 1

print(f"Quadrants: {quadrants} multiplied: {quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]}")


