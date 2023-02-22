# TODO: Verificar o Comparator do Java
# TODO: HashMap e Dictionary
import Lightpath
import Path
import json
from Slot import Slot
from PhysicalTopology import PhysicalTopology


class VirtualTopology:
    def __init__(self, json: json, pt: PhysicalTopology):
        if 'virtual-topology' in json:
            virtual_topology = json['virtual-topology']
            self.name = virtual_topology["name"]

        self.num_nodes = pt.get_num_nodes()
        self.lightpaths = {}
        # TODO: Entender onde essa estrutura >> adjMatrix << é utilizada
        self.adjMatrix = [[{} for n in range(self.nodes)] for n in range(self.nodes)]
        self.pt = pt
        self.next_lightpath_id = 0

    # TODO: Escolher entre ou dar suporte para Path ou Links+Slots
    def create_lightpath(self, path: Path, modulation_level: float):
        # TODO: Lidar com exceção

        if len(path.getLinks()) < 1:
            pass
        else:
            if self.can_create_lightpath(path.getSlotList(), modulation_level):
                self.create_lightpath_in_physical_topology(
                    path.getSlotList(), modulation_level)
                src = self.pt.getLink(path.getLink(0)).getSource()
                dst = self.pt.getLink(path.getLink(
                    path.getNumLinks()-1)).getDestination()
                if src == dst:
                    dst = self.pt.getLink(path.getLink(
                        path.getNumLinks() - 2)).getDestination()
                id = self.next_lightpath_id
                lp = Lightpath(id, src, dst, path, modulation_level)
                self.lightpaths[id] = lp
                self.next_lightpath_id += 1
                return id
            return -1

    def can_create_lightpath(self, slots: list[Slot], modulation_level: float) -> bool:
        for slot in slots:
            if not self.pt.get_link(slot.getLink()).isSlotAvailable(slot):
                return False
        return True

    def create_lightpath_in_physical_topology(self, slots: list[Slot], modulation_level: float) -> None:
        for slot in slots:
            self.pt.getLink(slot.getLink()).reserveSlot(slot)
            self.pt.getLink(slot.getLink()).setModulationLevel(
                slot, modulation_level)

    def remove_lightpath(self, id):
        if id < 0:
            # TODO: Desenvolver essa exceção
            pass
        else:
            if id not in self.lightpaths:
                return False
            self.lightpaths.pop(id)

    def get_lightpath(self, id):
        return self.lightpaths.get(id)
