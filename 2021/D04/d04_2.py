from typing import List

import numpy as np

from D04.Bingo import Board

with open('input_1.txt', 'r') as f:
#with open('example.txt', 'r') as f:
    arr = np.genfromtxt(f, dtype=str, delimiter='\n')

boards: List[Board] = []
currentBoard: Board = Board()
currentBoard.toString()

for i in range(1, len(arr)):
    line = arr[i].split()
    line = [int(line[i]) for i in range(0, len(line))]
    print(i, line)
    currentBoard.addRow(line)
    if (i % 5 == 0):
        boards.append(currentBoard)
        currentBoard.toString()
        currentBoard = Board()

numbers = arr[0].split(',')
numbers = [int(numbers[i]) for i in range(0, len(numbers))]
print("numbers", numbers)
lastBoard:Board = None
for i in range(0, len(numbers)):
    print("crossing=", numbers[i])

    boardsSolved = []
    for board in boards:
        board.crossNumber(numbers[i])
        if (board.isSolved()):
            boardsSolved.append(board)
            lastBoard = board
    boards = [board for board in boards if board not in boardsSolved]

    if len(boards) == 0 and lastBoard is not None:
        print(numbers[i], lastBoard.getScore(), numbers[i] * lastBoard.getScore())
        break
