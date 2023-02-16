from TrafficInfo import TrafficInfo
from Flow import Flow
from Event import ArrivalEvent, DepartureEvent
from random import randrange
from random import uniform
import random
import numpy as np
from util.Distribution import Distribution


class TrafficGenerator:
    def __init__(self, traffic, load):
        self.call = int(traffic['call'])
        self.load = int(traffic['load'])
        self.maxRate = int(traffic['max-rate'])
        self.n_types = len(traffic['calls'])

        self.totalWeight = 0
        self.meanRate = 0
        self.meanHoldingTime = 0

        self.callsType = np.empty((self.n_types,), dtype=TrafficInfo)

        for call in traffic['calls']:
            self.totalWeight += int(call['weight'])

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
        weightVector = np.empty((self.totalWeight,), dtype=int)
        aux = 0
        for i in range(self.n_types):
            for j in range(self.callsType[i].getWeight()):
                weightVector[aux] = i
                aux += 1

        meanArrivalTime = self.meanHoldingTime * (self.meanRate/self.maxRate) / self.load
        time = 0
        id = 0
        numNodes = pt.getNumNodes()
        dist1 = Distribution(1, seed)
        dist2 = Distribution(2, seed)
        dist3 = Distribution(3, seed)
        dist4 = Distribution(4, seed)

        for i in range(self.call):
            type = weightVector[dist1.nextInt(self.totalWeight)]
            src = dst = dist2.nextInt(numNodes)
            while src == dst:
                dst = dist2.nextInt(numNodes)

            holdingTime = dist4.nextExponential(self.callsType[type].getHoldingTime())
            newFlow = Flow(id, src, dst, time, self.callsType[type].getRate(), holdingTime,
                           self.callsType[type].getCos(), time+(holdingTime*0.5))

            # TODO: Herança para os tipos FlowArrivalEvent e FlowDepartureEvent
            event = ArrivalEvent('Arrival', newFlow, time)
            time += dist3.nextExponential(meanArrivalTime)
            events.addEvent(event)
            event = DepartureEvent('Departure', newFlow, time+holdingTime)
            events.addEvent(event)
            id += 1
