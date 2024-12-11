import re


def countBagsIn(bagName, bags):
    count = 1

    for inner in bags[bagName]:
        if len(inner)>0:
            inner = inner[0]
            print(inner, int(inner[0]), inner[1])
            count = count + int(inner[0])*countBagsIn(inner[1], bags)
    print('bagName=', bagName, "count=", count)
    return count

with open('input.txt', 'r') as f:
    lines = f.readlines()

pattern = re.compile("([0-9]+) ([a-z]+ [a-z]+)")
bags = {}
for line in lines:
    line = line.replace(" bags", "").replace(" bag", "").replace(".\n", "")
    outer, inner = line.split(' contain ')

    inner = inner.split(', ')
    inner = [pattern.findall(x) for x in inner]
    #print(outer, inner)
    bags[outer]=inner

print(bags)
print(countBagsIn('shiny gold', bags)-1)


