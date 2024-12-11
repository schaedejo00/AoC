from D02.Report import Report

count: int = 0
with open('input_1.txt', 'r') as f:
    while line := f.readline():
        report_data: list[int] = [int(x) for x in line.split(" ")]
        report: Report = Report(report_data)
        count += 1 if report.is_safe() or report.can_be_fixed()  else 0

print(count)






