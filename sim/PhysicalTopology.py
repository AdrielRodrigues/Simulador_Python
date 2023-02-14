import numpy as np

from Link import Link
from util.WeightedGraph import WeightedGraph


class PhysicalTopology:
    def __init__(self, pt):
        self.name = str(pt['name'])
        self.cores = int(pt['cores'])
        self.slots = int(pt['slots'])
        self.protection = bool(pt['protection'])
        self.sharing = bool(pt['sharing'])
        self.grooming = bool(pt['grooming'])
        self.slotsBandwidth = float(pt['slotsBandwidth'])

        # Sequência numérica de nós
        self.nodes = []

        for node in pt['nodes']:
            self.nodes.append(int(node))

        self.n_nodes = len(self.nodes)

        # Links em sequência e matriz adj
        self.links = []
        self.matrix = np.empty((self.n_nodes, self.n_nodes), dtype=Link)

        for link in pt['links']:
            obj = Link(link, self.cores, self.slots)
            self.links.append(obj)
            self.matrix[int(link['source'])][int(link['destination'])] = obj

        # Grafo
        self.graph = self.doWeightedGraph()

    def getSharing(self):
        return self.sharing

    def getGrooming(self):
        return self.grooming

    def getProtection(self):
        return self.protection

    def getNumNodes(self):
        return self.n_nodes

    def getNumCores(self):
        return self.cores

    def getSlotsCapacity(self):
        return self.slotsBandwidth

    def getNumLinks(self):
        return len(self.links)

    def getNumSlots(self):
        return self.slots

    def getLink(self, *args):
        # Array
        if len(args) == 1:
            return self.links[args[0]]
        # Matrix
        elif len(args) == 2:
            return self.matrix[args[0]][args[1]]

    def doWeightedGraph(self):
        g = WeightedGraph(self.n_nodes)
        # TODO: Verificar >> Antes usava dois for i,j pra percorrer toda a matrix
        for link in self.links:
            source = link.getSource()
            destination = link.getDestination()
            weight = link.getWeight()
            g.addEdge(source, destination, weight)
        return g

    def getGraph(self):
        return self.graph
