from collections import defaultdict


class UnweightedGraph:
    graph: defaultdict(list)

    def __init__(self, graph: dict() = None):
        if graph is None:
            graph = {}
        self.graph = graph

    def add_edge(self, start: str, end: str):
        neighbours: [str] = []
        if start in self.graph:
            neighbours = self.graph[start]
        neighbours.append(end)
        self.graph[start] = neighbours


    def __str__(self):
        keys = self.graph.keys()
        to_return = [{key: self.graph[key]} for key in keys]
        return "graph: " + str(to_return)

    def __repr__(self):
        return self.__str__()




