from operator import itemgetter
import re

f = open("input_1.txt", "r")
lines = f.read().split('\n')
validPasswds = 0

for line in lines:
    #print(line)
    tokens = re.split('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line)
    #print(tokens)
    min, max, char, passwd = itemgetter(1, 2, 3, 4)(tokens)
    print ('min={}, max={}, char={}, passwd={}'.format(min, max, char, passwd))

    if (bool(passwd[int(min)-1] == char) ^ bool(passwd[int(max)-1] == char)):
        validPasswds += 1
        print ('min={}, max={}, char={}, passwd={} valid'.format(min, max, char, passwd))

print ('valid passwds={}'.format(validPasswds))