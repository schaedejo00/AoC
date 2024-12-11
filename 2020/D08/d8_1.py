import re
import numpy as np

with open('input_tst.txt', 'r') as f:
    lines = f.readlines()

pgmCounter = 0
accu = 0
executedLines = np.zeros(len(lines))
pattern = re.compile("(nop|acc|jmp) ([+|-][0-9]+)")

while pgmCounter < len(lines):
    if executedLines[pgmCounter] == 1:
        break
    executedLines[pgmCounter] += 1
    matches = pattern.findall(lines[pgmCounter])
    print(matches)
    cmd, value = matches[0][0], int(matches[0][1])
    print("cmd={}, value={}".format(cmd, value))
    if cmd == 'nop':
        pgmCounter += 1
    if cmd == 'acc':
        accu += value
        pgmCounter += 1
    if cmd == 'jmp':
        pgmCounter += value

if pgmCounter >= len(lines):
    print("terminated")

else:
    print('loop with line=' + str(pgmCounter))

print("accu=" + str(accu))