import numpy as np

import ArrayTools

count: int = 0
matches: list[str] = ["MAS", "SAM"]


array: np.ndarray = np.array([list(line) for line in np.loadtxt('input_1.txt', dtype=str)])

for x in range(0, array.shape[0]-2):
    for y in range(0, array.shape[1]-2):
        #3x3 Arrays ausschneiden
        tmp: list[list[chr]] = array[x:x + 3, y:y + 3]

        #prüfen ob 3x3 Array MAS oder SAM in beiden Diagonalen hat
        diagonals: list[str] = ArrayTools.get_all_diagonals(tmp)
        diagonal: str = ''.join(diagonals[2])
        anti_diagonals: list[str] = ArrayTools.get_anti_diagonal(tmp)
        anti_diagonal: str = ''.join(anti_diagonals[2])
        if diagonal in matches and anti_diagonal in matches:
            count += 1


print(count)
