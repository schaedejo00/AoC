import re
import numpy as np


def evaluate(pgm):
    pgmCounter = 0
    accu = 0
    executedLines = np.zeros(len(pgm))
    pattern = re.compile("(nop|acc|jmp) ([+|-][0-9]+)")

    while pgmCounter < len(pgm):
        if executedLines[pgmCounter] == 1:
            break
        executedLines[pgmCounter] += 1
        matches = pattern.findall(pgm[pgmCounter])

        cmd, value = matches[0][0], int(matches[0][1])
        #print("cmd={}, value={}".format(cmd, value))
        if cmd == 'nop':
            pgmCounter += 1
        if cmd == 'acc':
            accu += value
            pgmCounter += 1
        if cmd == 'jmp':
            pgmCounter += value

    return pgmCounter >= len(pgm), accu


def changeOp(line):
    if 'nop' in line:
        line = line.replace('nop', 'jmp')
    elif 'jmp' in line:
        line = line.replace('jmp', 'nop')
    return line


with open('input.txt', 'r') as f:
    lines = f.readlines()

terminated, accumulator = evaluate(lines)
indexLastOpChanged = -1

while not terminated:

    for i in range(indexLastOpChanged+1, len(lines)):
        if 'nop' in lines[i] or 'jmp' in lines[i]:
            indexLastOpChanged = i
            lines[indexLastOpChanged] = changeOp(lines[indexLastOpChanged])
            break

    terminated, accumulator = evaluate(lines)
    print('indexLastOpChanged={}, terminated={}, accumulator={}'.format(indexLastOpChanged, terminated, accumulator))
    print(lines)
    lines[indexLastOpChanged] = changeOp(lines[indexLastOpChanged])

print(accumulator)
