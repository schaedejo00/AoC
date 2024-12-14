
import re

from AoCInputHelper import *
import numpy as np
import matplotlib.pyplot as plt

def plot(robots: list[tuple[int, int, int, int]], max_x: int, max_y: int, plot_number: int = 0):
    fig, ax = plt.subplots()
    for robot in robots:
        ax.plot(robot[0], robot[1], 'ro')
    ax.set_xlim(0, max_x)
    ax.set_ylim(0, max_y)
    ax.text(0.02, 0.98, f'Plot: {plot_number}', transform=ax.transAxes,
            verticalalignment='top', horizontalalignment='left',
            fontsize=12, fontweight='bold')
    plt.show()

# prepare input
input_data: list[str] = get_input(2024, 14).split("\n")
#input_data: list[str] = open('example.txt').read().split("\n")

pattern: str = r"p=(?P<p_x>-?\d+),(?P<p_y>-?\d+) v=(?P<v_x>-?\d+),(?P<v_y>-?\d+)"
pattern: re.Pattern[str] = re.compile(pattern)
max_x: int = 101
max_y: int = 103
seconds: int = 8000

robots: list[tuple[int, int, int, int]] = []
for line in input_data:
    match: re.Match = pattern.match(line)
    robot: tuple[int, int, int, int] = (int(match.group("p_x")), int(match.group("p_y")), int(match.group("v_x")), int(match.group("v_y")))
    robots.append(robot)


for j in range(seconds):
    for i, robot in enumerate(robots):
        robot = ((robot[0] + robot[2])%max_x, (robot[1] + robot[3])%max_y, robot[2], robot[3])
        robots[i] = robot

    # check if most robots are in the middle
    x:int = max_x//2
    robotCount = sum(1 for robot in robots if robot[0] <= x+15 and robot[0] >= x-15)
    if robotCount > len(robots)*0.51:
        plot(robots, max_x, max_y, j+1)





