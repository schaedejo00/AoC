import re
import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()

numbers = [int(x) for x in lines]
target = 248131121

#target = 127
for i in range(0, len(numbers)):
    found = False
    for j in range(2,len(numbers)-i):
        if sum(numbers[i:i+j]) == target:
            res = numbers[i:i+j]
            print(res)
            res.sort()
            print(res[0])
            print(res[len(res)-1])
            print((res[0] + res[len(res)-1]))




