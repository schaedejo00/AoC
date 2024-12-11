import re
import numpy as np

def performInstruction(inst, stacks):
    m = re.match(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", inst)
    count, fromIndex, toIndex = int(m.group(1)), int(m.group(2))-1, int(m.group(3))-1
    print('before', stacks, inst)
    stacks[toIndex].extend(stacks[fromIndex][-count:])
    stacks[fromIndex] = stacks[fromIndex][:len(stacks[fromIndex])-count]
    print('after', stacks, inst)


count = 0
with open('input_1.txt', 'r') as f:
    puzzleInput = []
    for line in f:
        line = line.replace('\n', '')
        if 'move' in line:
            puzzleInput.append(line)
        else:
            puzzleInput.append(list(line))

i = puzzleInput.index([])-1
init = np.array(puzzleInput[:i])
instructions = puzzleInput[i+2:]
stacks = []
for x in range(1, len(init[0]), 4):
    stack = [token for token in init[:,x] if token not in [' ','[',']']]
    stack.reverse()
    stacks.append(stack)

for instruction in instructions:
    performInstruction(instruction, stacks)

print(stacks)
solution = ''
for stack in stacks:
    solution+=stack[-1]

print(solution)