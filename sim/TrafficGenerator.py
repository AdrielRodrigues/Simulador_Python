from TrafficInfo import TrafficInfo
import Flow
import Event
from random import randrange
from random import uniform
import random
import numpy as np
from util.Distribution import Distribution


class TrafficGenerator:
    def __init__(self, traffic, load):
        self.call = int(traffic['call'])
        self.load = int(traffic['load'])
        self.maxrate = int(traffic['max-rate'])
        self.n_types = len(traffic['calls'])

        self.totalWeight = 0
        self.meanRate = 0
        self.meanHoldingTime = 0

        self.callsType = np.empty((self.n_types,), dtype=TrafficInfo)

        for call in traffic['calls']:
            self.totalWeight += float(call['weight'])

        count = 0
        for call in traffic['calls']:
            self.holdingTime = float(call['holding-time'])
            self.rate = int(call['rate'])
            self.cos = int(call['cos'])
            self.weight = int(call['weight'])
            self.meanRate = float(self.rate) * (float(self.weight)/float(self.totalWeight))
            self.meanHoldingTime += self.holdingTime * float(self.weight) / float(self.totalWeight)

            self.callsType[count] = TrafficInfo(self.holdingTime, self.rate, self.cos, self.weight)

            count += 1

    def generateTraffic(self, pt, events, seed):
        self.meanArrivalTime = self.holdingTime * (self.meanRate/self.maxrate) / self.load
        time = 0
        id = 0
        numNodes = pt.getNumNodes()
        dist1 = Distribution(1, seed)
        dist2 = Distribution(2, seed)
        dist3 = Distribution(3, seed)
        dist4 = Distribution(4, seed)

        for i in range(self.call):
