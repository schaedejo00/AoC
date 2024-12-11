import numpy as np
import re



with open('input_1.txt', 'r') as f:
    arr = np.genfromtxt(f, dtype=int, delimiter='\n')


for i in range(0,len(arr)):
    for j in range(0, len(arr)):
        for k in range(0, len(arr)):
            if(arr[i]+arr[j]+arr[k]==2020):
                print(arr[i]*arr[j]*arr[k])
                break
