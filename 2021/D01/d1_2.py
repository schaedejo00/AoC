import numpy as np
import re

with open('input_1.txt', 'r') as f:
    arr = np.genfromtxt(f, dtype=int, delimiter='\n')
previous = arr[0]

diff = np.zeros(len(arr))
count = 0
size = 3
for i in range(size, len(arr)):
    sum1 = np.sum(arr[i-size:i])
    sum2 = np.sum(arr[i-(size-1):i+1])

    if (sum2 > sum1):
        count+=1
    print(arr[i-3:i], sum1, arr[i-2:i+1], sum2, count)

print (count)


