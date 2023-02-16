from PhysicalTopology import PhysicalTopology
from VirtualTopology import VirtualTopology
from EventScheduler import EventScheduler
from TrafficGenerator import TrafficGenerator
import json
import time
'''
    Centralizes the simulation execution. Defines what the command line
    arguments do, and extracts the simulation information from the XML file.
'''


class Simulator:
    def __init__(self):
        self.trace = None
        self.verbose = None
        self.failure = None

    def execute(self, simConfigFile, trace, verbose, failure, forcedLoad, simulationNumbers):
        self.trace = trace
        self.verbose = verbose
        self.failure = failure

        # Read JSON file
        file = open(simConfigFile)
        data = json.load(file)

        for seed in range(1, simulationNumbers + 1, 1):

            print(f"=============== Simulation {seed}: Load {forcedLoad} ===============")

            begin = round(time.time() * 1000)
            pt = PhysicalTopology(data['physical-topology'])

            begin = round(time.time() * 1000)
            vt = VirtualTopology(data['virtual-topology'], pt)

            begin = round(time.time() * 1000)
            events = EventScheduler()
            traffic = TrafficGenerator(data['traffic'], forcedLoad)
            traffic.generateTraffic(pt, events, seed)

            events.getEvents().sort()
            file.close()

        return 1
