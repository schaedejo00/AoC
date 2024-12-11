import re
import numpy as np

with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [int(x) for x in lines]
lines.sort()
print(lines)

maxValue = 0
diffs = np.zeros(4, dtype=int)
adaptersUsed = [0]

for adapter in lines:
    maxValue = adaptersUsed[-1]
    #print('a={}, b={}, diff={}'.format(maxValue, adapter, adapter-maxValue))
    diffs[adapter-maxValue]+=1
    adaptersUsed.append(adapter)

diffs[3]+=1 #your Adapter
print(adaptersUsed)
print(diffs)

print(diffs[1]*diffs[3])
