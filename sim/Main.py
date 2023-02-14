import sys
from Simulator import Simulator


def main():
    print(sys.argv)
    args_size = len(sys.argv)
    # Parameters: ../xml/MSP-nsf.json 10 100 500 50
    usage = 'Usage: flexgridsim [simulation_file] [seed] [minload maxload step] [-trace] [-verbose] [-failure]'

    trace = False
    verbose = False
    failure = False

    if args_size < 6 or args_size > 9:
        print(usage)
        exit(0)
    else:
        simConfigFile = sys.argv[1]
        seed = int(sys.argv[2])
        minload = int(sys.argv[3])
        maxload = int(sys.argv[4])
        step = int(sys.argv[5])

        if 'trace' in sys.argv:
            trace = True
        if 'verbose' in sys.argv:
            verbose = True
        if 'failure' in sys.argv:
            failure = True

        for load in range(minload, maxload + step, step):
            sim = Simulator()
            sim.execute(simConfigFile, trace, verbose, failure, load, seed)


if __name__ == '__main__':
    main()
