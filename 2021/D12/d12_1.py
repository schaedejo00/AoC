from D12.CavePath import CavePath
from D12.UnweightedGraph import UnweightedGraph

#with open('example3.txt', 'r', encoding="utf-8") as f:
with open('input_1.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")

graph: UnweightedGraph = UnweightedGraph()


for line in puzzleInput:
    start, end = line.split("-")
    graph.add_edge(start, end)
    graph.add_edge(end, start)
path: CavePath = CavePath()
paths = path.get_all_path(graph, "start", "end", 2)
#print(graph)
print(len(paths))



