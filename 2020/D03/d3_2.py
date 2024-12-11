import numpy as np
import re

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def to_str(self):
        return ('({0}, {1})'.format(self.x, self.y))

def stringTo2DimArray(str):
    arr = list(content)

    #save line size and column count then split list of lines into separate chars
    yDim = arr.count('\n')+1
    xDim = arr.index('\n')
    arr = list(filter(lambda a: a != '\n', arr))

    #reshape array to match line size and column count
    arr = np.array(arr)
    arr = arr.reshape(yDim,xDim)
    return arr

def countOccurence(arr, char, stepX, stepY):
    pos = Point(stepX, stepY)
    maxDim = arr.shape
    counter = 0
    #print('dimx={}, dimy={}'.format(maxDim[0], maxDim[1]))

    while pos.y < maxDim[0]:

        if (arr[pos.y, pos.x] == char):
            counter += 1

        pos.x = (pos.x + stepX) % maxDim[1]
        pos.y = pos.y + stepY


    print('treeCount={}, for stepX={}, stepY={}'.format(counter, stepX, stepY))
    return counter



with open('input_1.txt', 'r') as f:
    content = f.read()
    arr = stringTo2DimArray(content)

product = 1
steps = [[1,1],
         [3,1],
         [5,1],
         [7,1],
         [1,2]]
i=0
while i < len(steps):
    product *= countOccurence(arr, '#', steps[i][0], steps[i][1])
    i+=1

print(product)
