from PhysicalTopology import PhysicalTopology
from VirtualTopology import VirtualTopology
from EventScheduler import EventScheduler
from TrafficGenerator import TrafficGenerator
import json
import time

'''
    Centralizes the simulation execution. Defines what the command line
    arguments do, and extracts the simulation information from the JSON file.
'''


class Simulator:
    sim_name = 'SimPy'
    sim_version = 1.0
    divider = "="*33

    def __init__(self):
        self.trace = False
        self.verbose = False
        self.failure = False

    def execute(self, sim_config_file: str, number_of_simulations: int, trace: bool, verbose: bool, failure: bool, forced_load: int):
        self.trace = trace
        self.verbose = verbose
        self.failure = failure

        if (self.verbose):
            print(self.divider)
            print(
                f"== Simulator {self.sim_name} version {self.sim_version} ==")
            print(f"{self.divider}\n")

        if (self.verbose):
            print(f"Accessing simulation file {sim_config_file} ...")

        with open(sim_config_file) as file:
            sim_config_file_as_dict = json.load(file)

            begin = round(time.time() * 1000)
            pt = PhysicalTopology(sim_config_file_as_dict['physical-topology'])
            end = round(time.time() * 1000)
            if verbose:
                print(f"Time to build Physical Topology: {end - begin}ms")

            begin = round(time.time() * 1000)
            vt = VirtualTopology(
                sim_config_file_as_dict['virtual-topology'], pt)
            end = round(time.time() * 1000)
            if verbose:
                print(f"Time to build Virtual Topology: {end - begin}ms")

        for seed in range(1, number_of_simulations + 1):
            print(
                f"=============== Simulation {seed}: Load {forced_load} ===============")

        return 1
