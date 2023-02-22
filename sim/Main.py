import argparse
import os
from typing import List, Optional
from Simulator import Simulator


class Main:
    @staticmethod
    def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description='Simulator for Space Division Multiplexing Elastic Optical Networks')

        parser.add_argument('simConfigFile', type=str,
                            help='Simulation configuration file')
        parser.add_argument(
            'seeds', type=int, help='Number of seeds for random number generator')

        parser.add_argument(
            '-t', '--trace', action='store_true', help='Enable trace')
        parser.add_argument('-v', '--verbose',
                            action='store_true', help='Enable verbose output')

        parser.add_argument('-f', '--failure', action='store_true',
                            help='Enable network failure simulation')
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
        seeds = args.seeds
        trace = args.trace
        verbose = args.verbose
        failure = args.failure

        min_load = args.minload
        max_load = args.maxload
        step = args.step

        if min_load is None:
            min_load = 0
        if max_load is None:
            max_load = 0
        if step is None:
            step = 1

        for load in range(min_load, max_load + step, step):
            # try:
            sim = Simulator()
            sim.execute(sim_config_file, seeds, trace,
                        verbose, failure, load)
            # except Exception as e:
            #     print(f"Error executing simulation: {e}")
            #     return


if __name__ == '__main__':
    args = Main.parse_args()
    Main.run(args)
