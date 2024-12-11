import numpy as np
import re

with open('input_1.txt', 'r') as f:
    arr = np.genfromtxt(f, dtype=int, delimiter='\n')
previous = arr[0]

diff = np.zeros(len(arr))
count = 0

for i in range(1, len(arr)):
    diff[i] = arr[i] - previous
    previous = arr[i]
    if (diff[i] > 0):
        count+=1
    print(arr[i], diff[i], count)

print (count)


