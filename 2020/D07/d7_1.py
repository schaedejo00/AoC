from graph_tools import Graph
import re

#work in progress

with open('input_tst2.txt', 'r') as f:
    lines = f.readlines()

g = Graph(directed=True)
pattern = re.compile("([a-z]+ [a-z]+) bags contain (( ?[0-9]+ [a-z]+ [a-z]+ bags?,?)+| ?no other bags)\.")
neighbourPattern = re.compile("(([0-9]+ [a-z]+ [a-z]+) bags?,?)+")
for line in lines:
    matches = pattern.findall(line)
    print(matches[0][0])

    start = matches[0][0]
    neighbours = matches[0][1]



    g.add_vertex(start)

    if neighbours != 'no other bags':
        nMatches = neighbourPattern.findall(neighbours)
        print(nMatches)

