import numpy as np


class WeightedGraph:
    def __init__(self, n):
        self.numNodes = n
        self.edges = np.full((self.numNodes, self.numNodes), 0, dtype=float)
        self.edgeRemoved = np.full((self.numNodes, self.numNodes), False, dtype=bool)
        visited = []

    def addEdge(self, source, destination, weight):
        self.edges[source][destination] = weight

    def neighbors(self, vertex):
        answer = []
        counter = 0
        for e in self.edges[vertex]:
            if e is not None and e > 0:
                answer.append(counter)
            counter += 1
        return answer

    def getNumNodes(self):
        return self.numNodes

    def getNumEdges(self):
        return len(self.edges)

    def getWeight(self, source, destination):
        return self.edges[source][destination]
