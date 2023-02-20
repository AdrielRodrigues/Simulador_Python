import argparse
import os
from typing import List, Optional
from Simulator import Simulator

class Main:
    @staticmethod
    def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
        parser = argparse.ArgumentParser(description='Simulator for elastic optical networks with spatial division multiplexing')

        parser.add_argument('simConfigFile', type=str, help='Simulation configuration file')
        parser.add_argument('seed', type=int, help='Seed for random number generator')

        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument('-t', '--trace', action='store_true', help='Enable trace')
        group.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')

        parser.add_argument('-f', '--failure', action='store_true', help='Enable link failure simulation')
        parser.add_argument('--minload', type=int, help='Minimum load')
        parser.add_argument('--maxload', type=int, help='Maximum load')
        parser.add_argument('--step', type=int, help='Load step')

        return parser.parse_args(args)

    @staticmethod
    def validate_args(args: argparse.Namespace) -> bool:
        if not os.path.isfile(args.simConfigFile):
            print(f"File {args.simConfigFile} not found")
            return False

        if args.minload is None and args.maxload is None and args.step is None:
            return True

        if args.minload is not None and args.maxload is not None and args.step is not None:
            return True

        print("Error: minload, maxload and step must be specified together")
        return False

    @staticmethod
    def run(args: argparse.Namespace) -> None:
        if not Main.validate_args(args):
            return

        sim_config_file = args.simConfigFile
        seed = args.seed
        trace = args.trace
        verbose = args.verbose
        failure = args.failure

        minload = args.minload
        maxload = args.maxload
        step = args.step

        if minload is None:
            minload = 0
        if maxload is None:
            maxload = 0
        if step is None:
            step = 1

        for load in range(minload, maxload + step, step):
            try:
                sim = Simulator()
                sim.execute(sim_config_file, trace, verbose, failure, load, seed)
            except Exception as e:
                print(f"Error executing simulation: {e}")
                return

if __name__ == '__main__':
    args = Main.parse_args()
    Main.run(args)
