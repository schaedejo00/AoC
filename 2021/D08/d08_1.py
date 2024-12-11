from collections import defaultdict
from typing import List

import numpy as np

from D05.Point import Point

def initializeDict() -> dict():
    dictionary = defaultdict(list)
    dictionary[2] = [1]
    dictionary[3] = [7]
    dictionary[4] = [4]
    dictionary[5] = [2, 3, 5]
    dictionary[6] = [0, 6, 9]
    dictionary[7] = [8]
    return dictionary

# with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

counter = 0

digitLengthToDigits = initializeDict()

for line in puzzleInput:
    signalArr, outputArr = [["".join(sorted(digit)) for digit in token.strip().split(" ")] for token in
                            line.strip().split("|")]
    newDict = defaultdict(list)
    for digit in signalArr:
        newDict[digit] = digitLengthToDigits[len(digit)]

    for token in outputArr:
        numbers = newDict.get(token)
        if len(numbers) == 1 and numbers[0] in [1, 4, 7, 8]:
            counter += 1
print(counter)
