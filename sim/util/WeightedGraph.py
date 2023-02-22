import numpy as np


class WeightedGraph:
    def __init__(self, num_of_nodes):
        self.num_of_nodes = num_of_nodes
        self.edges = np.full((self.num_of_nodes, self.num_of_nodes), None)

    def add_edge(self, source, destination, weight):
        self.edges[source][destination] = weight

    def neighbors(self, vertex):
        answer = []
        counter = 0
        for e in self.edges[vertex]:
            if e is not None and e > 0:
                answer.append(counter)
            counter += 1
        return answer

    def get_num_of_nodes(self):
        return self.num_of_nodes

    def get_num_of_edges(self):
        return len(self.edges)

    def get_weight(self, source, destination):
        return self.edges[source][destination]
