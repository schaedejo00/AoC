import re
import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()

numbers = [int(x) for x in lines]
valids = []
preambleLen = 25
print(numbers)

for i in range(preambleLen, len(numbers)):
    valid = False
    for j in range(-preambleLen,0):
        for k in range(-preambleLen,0):
            if j == k:
                continue
            if numbers[i] == numbers[i+j]+numbers[i+k]:
                valids.append(numbers[i])
                print('valid={}, sum={}+{}, index={}/{}'.format(numbers[i], numbers[i+j], numbers[i+k], i+j, i+k))
                break
        if valid: break

print([x for x in numbers[preambleLen:len(numbers)] if x not in valids])

