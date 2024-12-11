from functools import reduce


import numpy as np
from Tools import Tools



with open('input_1.txt', 'r') as f:
#with open('example.txt', 'r') as f:
    arr = np.genfromtxt(f, dtype=str, delimiter='\n')


arr = [Tools.strListToIntList(list(arr[i])) for i in range(0, len(arr))]
arr = np.transpose(arr)


rateColumns = len(arr)
count = np.zeros(rateColumns).astype(int)
gamma = np.zeros(rateColumns).astype(int)
epsilon = np.zeros(rateColumns).astype(int)

maxCount = len(arr[0])
for i in range(0, rateColumns):
    count[i] = reduce(lambda a, b: int(a+b), arr[i])
    if(count[i] > maxCount/2):
        gamma[i] = 1
    epsilon[i] = 1 if (gamma[i]==0) else 0

gamma = Tools.interpretIntListAsBinaryNumber(gamma)
epsilon = Tools.interpretIntListAsBinaryNumber(epsilon)
print(arr, maxCount, count, gamma, epsilon, gamma*epsilon)





