from typing import List
from Tools import Tools

import numpy as np

def getRating(data: List[List[int]], mostCommon:bool) -> int:
    iterationNr = 0

    while (len(data) > 1):
        relevantColumn = [row[iterationNr] for row in data]
        countOfOnes = len([True for i in range(0, len(relevantColumn)) if relevantColumn[i]==1])
        countOfZeros = len(relevantColumn) - countOfOnes
        mostCommonValue = 1 if countOfOnes >= countOfZeros else 0
        print(relevantColumn, countOfOnes, countOfZeros)
        newData = []
        for row in data:
            if mostCommon and row[iterationNr] == mostCommonValue:
                newData.append(row)
            if not mostCommon and row[iterationNr] != mostCommonValue:
                newData.append(row)
        data = newData
        iterationNr += 1

    return Tools.interpretIntListAsBinaryNumber(data[0])

with open('input_1.txt', 'r') as f:
#with open('example.txt', 'r') as f:
    arr = np.genfromtxt(f, dtype=str, delimiter='\n')

arr = [Tools.strListToIntList(list(arr[i])) for i in range(0, len(arr))]

oxyRating = getRating(arr, True)
co2Rating = getRating(arr, False)



print(oxyRating, co2Rating, oxyRating * co2Rating)