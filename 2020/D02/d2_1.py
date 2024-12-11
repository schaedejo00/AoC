#from operator import itemgetter
import re

with open('input_1.txt') as f:
   lines = f.read().split('\n')

validPasswds = 0

for line in lines:
    print(line)
    tokens = re.split('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line)
    print(tokens)
    #min, max, char, passwd = itemgetter(1, 2, 3, 4)(tokens)
    #List comprehensions
    #NumPy
    #=> compile to C => ???
    min, max, char, passwd = int(tokens[1]), int(tokens[2]), tokens[3], tokens[4]
    print ('min={}, max={}, char={}, passwd={}'.format(min, max, char, passwd))

    count = passwd.count(char)
    if (min <= count and count <= max):
        validPasswds += 1

print ('valid passwds={}'.format(validPasswds))