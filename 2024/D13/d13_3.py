import sys
from typing import Iterator

from AoCInputHelper import *
import re
from sympy import factorint
from ortools.linear_solver import pywraplp


def solve_optimization_problem(x_a:int, x_b:int, y_a:int, y_b:int, x_ges:int, y_ges:int) -> tuple[int, int, int]:
    solver = pywraplp.Solver.CreateSolver('SCIP') #Ganzzahlige Lineare Optimierung

    # Variablen definieren
    n:int = solver.NumVar(0, solver.infinity(), 'n')
    m:int = solver.NumVar(0, solver.infinity(), 'm')
    solver.Add(n == solver.IntVar(0, solver.infinity(), 'n_int')) #Ganzzahlige Lösung erzwingen
    solver.Add(m == solver.IntVar(0, solver.infinity(), 'm_int')) #Ganzzahlige Lösung erzwingen

    # Nebenbedingungen hinzufügen
    solver.Add(n * x_a + m * x_b == x_ges)
    solver.Add(n * y_a + m * y_b == y_ges)

    # Zielfunktion definieren
    solver.Minimize(3 * n + m)

    # Problem lösen
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        return n.solution_value(), m.solution_value(), solver.Objective().Value()
    else:
        return None, None, None

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
    coordinates_prize: tuple[int, int] = (int(match.group("x_prize"))+10000000000000 , int(match.group("y_prize"))+10000000000000)


    n, m, cost = solve_optimization_problem(coordinates_a[0], coordinates_b[0], coordinates_a[1], coordinates_b[1], coordinates_prize[0], coordinates_prize[1])

    if cost is not None:
        print(f"coordinates_a={coordinates_a}, coordinates_b={coordinates_b}, coordinates_prize={coordinates_prize}")
        print(f"Solution found: A pressed {n} times, B pressed {m} times, cost={cost}")
        costs.append(cost)

#print(f"costs={costs}, sum={sum(costs)}")
print(f"sum={sum(costs)}")

