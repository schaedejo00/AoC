import numpy as np

def get_all_diagonals(array) -> list:
    array = np.array(array)
    rows, cols = array.shape
    diagonals: list = []

    for offset in range(-rows + 1, cols):
        diagonal: list = np.diag(array, k=offset)
        if len(diagonal) > 0:
            diagonals.append(diagonal)

    return diagonals

def get_anti_diagonal(array) -> list:
    flipped: list = np.fliplr(array)
    return get_all_diagonals(flipped)

def get_all_columns(array) -> list:
    array = np.array(array)
    column_count: int = array.shape[1]
    to_return: list = [array[:, i] for i in range(column_count)]
    return to_return