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

        self.free_slots = np.ones((self.cores, self.slots), dtype=bool)
        self.can_be_shared = np.ones((self.cores, self.slots), dtype=bool)

        self.modulation_level = np.full(
            (self.cores, self.slots), 10, dtype=float)
        self.noise = np.full((self.cores, self.slots), 10, dtype=float)

    def get_spectrum(self, *args):
        if len(args) == 0:
            return self.free_slots
        elif len(args) == 1:
            return self.free_slots[args[0]]
        elif len(args) == 2:
            return self.free_slots[args[0]][args[1]]

    def get_id(self):
        return self.id

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dst

    def get_weight(self):
        return self.weight

    def get_delay(self):
        return self.delay

    def is_slot_available(self, slot):
        if self.free_slots[slot.getCore()][slot.getSlot()]:
            return True
        return False

    def reserve_slot(self, slot):
        self.free_slots[slot.getCore()][slot.getSlot()] = False

    def release_slot(self, slot):
        self.free_slots[slot.getCore()][slot.getSlot()] = True

    def set_modulation_level(self, slot, modulation):
        self.modulation_level[slot.getCore()][slot.getSlot()] = modulation
