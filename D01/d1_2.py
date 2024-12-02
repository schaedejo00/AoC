import numpy as np
import numpy.typing as npt

coordinates: npt.NDArray[np.int32] = None
with open('input_1.txt', 'r') as f:
    coordinates = np.loadtxt('input_1.txt', usecols=(0, 1), dtype=int)

coordinates.sort(axis=0)
print(coordinates)

left: np.ndarray = coordinates[:, 0]
right: np.ndarray = coordinates[:, 1]

counts: list[int, int] = [[int(x), np.count_nonzero(right == x)] for x in left]
value: int = sum([x * y for x, y in counts])

print(counts)
print(value)
