import numpy as np
import json
from Link import Link
from util.WeightedGraph import WeightedGraph


class PhysicalTopology:
    def __init__(self, pt: json):
        self.name = str(pt['name'])
        self.cores = int(pt['cores'])
        self.slots = int(pt['slots'])
        self.protection = bool(pt['protection'])
        self.sharing = bool(pt['sharing'])
        self.grooming = bool(pt['grooming'])
        self.slots_bandwidth = float(pt['slotsBandwidth'])

        # Sequência numérica de nós
        self.nodes = []

        for node in pt['nodes']:
            self.nodes.append(int(node))

        self.num_of_nodes = len(self.nodes)

        # Links em sequência e matriz adj
        self.links = []
        self.adjacency_matrix = np.empty(
            (self.num_of_nodes, self.num_of_nodes), dtype=Link)

        for link in pt['links']:
            source_node = int(link['source'])
            destination_node = int(link['destination'])

            current_link = Link(link, self.cores, self.slots)
            self.links.append(current_link)
            self.adjacency_matrix[source_node][destination_node] = current_link

        # Grafo
        self.graph = self.__do_weighted_graph()

    def get_grooming(self) -> bool:
        return self.grooming

    def get_protection(self) -> bool:
        return self.protection

    def get_num_nodes(self) -> int:
        return self.num_of_nodes

    def get_num_cores(self) -> int:
        return self.cores

    def get_slots_capacity(self) -> float:
        return self.slots_bandwidth

    def get_num_links(self) -> int:
        return len(self.links)

    def get_num_slots(self) -> int:
        return self.slots

    def get_link(self, *args) -> Link:
        if len(args) == 1:
            return self.links[args[0]]
        # Matrix
        elif len(args) == 2:
            return self.adjacency_matrix[args[0]][args[1]]

    def __do_weighted_graph(self) -> WeightedGraph:
        graph = WeightedGraph(self.num_of_nodes)
        for i in range(self.num_of_nodes):
            for j in range(self.num_of_nodes):
                if self.adjacency_matrix[i][j] is not None:
                    graph.add_edge(
                        i, j, self.adjacency_matrix[i][j].get_weight())
        return graph

    def get_graph(self):
        return self.graph
