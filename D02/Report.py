import numpy as np


class Report:

    def __init__(self, data: list[int]):
        self.data = data

    def is_safe(self) -> bool:
        return self.__is_safe(self.data)

    @staticmethod
    def __is_safe(report: list[int]) -> bool:
        last_diff: int = report[1] - report[0]
        for i in range(1, len(report)):
            diff = report[i] - report[i - 1]
            if abs(diff) not in [1, 2, 3] or np.sign(diff) != np.sign(last_diff):
                return False
            last_diff = diff
        return True

    def can_be_fixed(self) -> bool:
        for i in range(0, len(self.data)):
            fixed_report: list[int] = self.data.copy()
            fixed_report.pop(i)
            if Report.__is_safe(fixed_report):
                return True
        return False