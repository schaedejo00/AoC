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


def refineDictionary(dictionary:dict()):
    # refining the dictionary
    numberDict = defaultdict(list)
    while len(dictionary.keys()) > len(numberDict.keys()):
        # Aktuialisieren des eines Dictionarys von gefundenen Zahlen zu Buchstabenkombinationen
        for key in dictionary.keys():
            value = dictionary[key]
            if len(value) == 1:
                numberDict[value[0]] = key

        for key in dictionary.keys():
            value = dictionary[key]

            if len(key) == 5:
                # Möglichkeiten [2, 3, 5]
                if np.all(np.isin(list(numberDict[1]), list(key))):
                    # ist eine 3
                    dictionary[key] = [3]
                else:
                    str4MinusStr1 = np.setdiff1d(list(numberDict[4]), list(numberDict[1]))
                    if np.all(np.isin(str4MinusStr1, list(key))):
                        dictionary[key] = [5]
                    else:
                        dictionary[key] = [2]
            elif len(key) == 6:
                # Möglichkeiten [0, 6, 9]
                if not np.all(np.isin(list(numberDict[1]), list(key))):
                    # ist eine 6
                    dictionary[key] = [6]
                else:
                    # kann erst entschieden werden, wenn die 3 gefunden wurde
                    if numberDict.__contains__(3):
                        if np.all(np.isin(list(numberDict[3]), list(key))):
                            # ist eine 9
                            dictionary[key] = [9]
                        else:
                            # ist eine 0
                            dictionary[key] = [0]
        #print(dictionary, numberDict)


# with open('example.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

numbers = []
digitLengthToDigits = initializeDict()

for line in puzzleInput:
    signalArr, outputArr = [["".join(sorted(digit)) for digit in token.strip().split(" ")] for token in line.strip().split("|")]

    newDict = defaultdict(list)

    for digit in signalArr:
        newDict[digit] = digitLengthToDigits[len(digit)]

    refineDictionary(newDict)

    number = ""
    for token in outputArr:
        number += str(newDict.get(token)[0])

    numbers.append(int(number))

print(sum(numbers), numbers)
