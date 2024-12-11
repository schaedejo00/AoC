import numpy as np

coordinates: np.ndarray = np.loadtxt('input_1.txt', usecols=(0, 1), dtype=int)

coordinates.sort(axis=0)
print(coordinates)

diffs: list[int] = [int(abs(x - y)) for x, y in coordinates]

print(diffs)
print(sum(diffs))
