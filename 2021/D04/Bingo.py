from typing import List


class Board:
    def __init__(self):
        self.board: List[List[int]] = []

    def addRow(self, row: List[int]):
        self.board.append(row)

    def toString(self):
        print(self.board)

    def isSolved(self) -> bool:
        for i in range(0, len(self.board)):
            column = [row[i] for row in self.board]
            if column.count(-1) == len(column):
                return True
        for row in self.board:
            if row.count(-1) == len(row):
                return True

        return False

    def crossNumber(self, number: int):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if self.board[i][j] == number:
                    self.board[i][j] = -1

    def getScore(self) -> int:
        relevantNumbers = [num for row in self.board for num in row if num > 0]
        return sum(relevantNumbers)
