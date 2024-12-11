import numpy as np

import ArrayTools

count: int = 0
pattern: str = r"XMAS"
reversed_pattern: str = pattern[::-1]


array: np.ndarray = [list(line) for line in np.loadtxt('input_1.txt', dtype=str)]

#Zeilen vorwärts und rückwärts durchgehen
for line in array:
    line = ''.join(line)
    count += line.count(pattern)
    count += line.count(reversed_pattern)
print(count)

#Spalten durchgehen vorwärts und rückwärts durchgehen
colums: list[str] = ArrayTools.get_all_columns(array)
for column in colums:
    column = ''.join(column)
    count += column.count(pattern)
    count += column.count(reversed_pattern)
print(count)

#Diagonalen durchgehen
diagonals: list[str] = ArrayTools.get_all_diagonals(array)
for diagonal in diagonals:
    diagonal = ''.join(diagonal)
    count += diagonal.count(pattern)
    count += diagonal.count(reversed_pattern)
print(count)

#Antidiagonale durchgehen
antidiagonals: list[str] = ArrayTools.get_anti_diagonal(array)
for antidiagonal in antidiagonals:
    antidiagonal = ''.join(antidiagonal)
    count += antidiagonal.count(pattern)
    count += antidiagonal.count(reversed_pattern)

print(count)
