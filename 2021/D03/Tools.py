from functools import reduce
from typing import List


class Tools:
    @staticmethod
    def strListToIntList(data: List[str]) -> List[int]:
        return [int(item) for item in data]

    @staticmethod
    def interpretIntListAsBinaryNumber(data: List[int]) -> int:
        strList = reduce(lambda a, b: a + b, [str(i) for i in data])
        return int(strList, 2)

    @staticmethod
    def countValueOccurence(data: List[int], value: int) -> int:
        count = len([True for i in range(0, len(data)) if data[i] == value])
        return count
