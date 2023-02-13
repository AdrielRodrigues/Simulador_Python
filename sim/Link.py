import numpy as np


class Link:
    def __init__(self, link, cores, slots):
        self.cores = cores
        self.slots = slots

        self.id = int(link['id'])
        self.src = int(link['source'])
        self.dst = int(link['destination'])
        self.delay = float(link['delay'])
        self.bandwidth = float(link['bandwidth'])
        self.weight = float(link['weight'])
        # TODO: Verificar as situações onde weight e distance não são a mesma coisa
        self.distance = float(link['weight'])

        self.active = True

        self.freeSlots = np.ones((self.cores, self.slots), dtype=bool)
        self.canBeShared = np.ones((self.cores, self.slots), dtype=bool)

        self.modulationLevel = np.full((self.cores, self.slots), 10, dtype=float)
        self.noise = np.full((self.cores, self.slots), 10, dtype=float)

    def getSpectrum(self, *args):
        if len(args) == 0:
            return self.freeSlots
        elif len(args) == 1:
            return self.freeSlots[args[0]]
        elif len(args) == 2:
            return self.freeSlots[args[0]][args[1]]

    def getID(self):
        return self.id

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dst

    def getWeight(self):
        return self.weight

    def getDelay(self):
        return self.delay

    def isSlotAvailable(self, slot):
        if self.freeSlots[slot.getCore()][slot.getSlot()]:
            return True
        return False

    def reserveSlot(self, slot):
        self.freeSlots[slot.getCore()][slot.getSlot()] = False

    def releaseSlot(self, slot):
        self.freeSlots[slot.getCore()][slot.getSlot()] = True

    def setModulationLevel(self, slot, modulation):
        self.modulationLevel[slot.getCore()][slot.getSlot()] = modulation
