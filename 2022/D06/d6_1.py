import re
import numpy as np

def isTokenValid(token):
    #print(token, len(token))
    for i in range(0, len(token)):
        count = token.count(token[i])
        #print(token, token[i], count)
        if count > 1:
            return False
    return True

with open('input_1.txt', 'r') as f:
    msg = f.readline().replace('\n', '')


sequenceLength = 4-1

for i in range(sequenceLength, len(msg)):
    sequence = msg[i-sequenceLength:i+1]
    if isTokenValid(sequence):
        print(i+1)
        break
    
print(msg)