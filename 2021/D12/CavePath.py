import numpy as np

from D12.UnweightedGraph import UnweightedGraph


class CavePath:

    @staticmethod
    def get_all_path(graph: UnweightedGraph, fromNode: str, toNode: str, max_small_cave_visit: int = 1) -> list[list[str]]:
        openPaths: list[list[str]] = [[fromNode]]
        endingPaths: list[list[str]] = []
        while len(openPaths) > 0:
            #currentPath als Queue nutzen und von vorne entleeren
            currentPath: list[str] = openPaths.pop(0)
            currentNode: str = currentPath[-1]
            currentNeighbours: [str] = []
            if currentNode in graph.graph.keys():
                currentNeighbours = graph.graph[currentNode]
            for neighbour in currentNeighbours:
                if neighbour == fromNode:
                    continue
                newPath: list[str] = currentPath.copy()
                newPath.append(neighbour)

                if not CavePath.is_small_cave_criteria_ok(newPath, max_small_cave_visit):
                    continue

                if len(newPath) > len(currentPath):
                    if newPath[-1] == toNode:
                        endingPaths.append(newPath)
                    elif newPath not in endingPaths:
                        openPaths.append(newPath)
        return endingPaths

    @staticmethod
    def is_small_cave_criteria_ok(path: str, max_small_cave_visit: int = 1):
        #Neueste Höhle ist UpperCase => keine neue Prüfung nötig
        if path[-1].isupper() or path[-1] == "end":
            return True

        lower_case_caves = [cave for cave in path if cave.islower()]
        unique, counts = np.unique(lower_case_caves, return_counts=True)

        for i in range(0, len(counts)):
            if 1 < counts[i] <= max_small_cave_visit:
                counts[i] = 1
                break

        for count in counts:
            if count > 1:
                return False
        return True
        #return all([True if n <= 1 else False for n in counts])
