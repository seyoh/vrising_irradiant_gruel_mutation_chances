import argparse
import sys

from Simulator import repeatAndCount, SimulateN
from calculator import calculateChanceOfSuccess


def parseArgs():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    simulate = subparsers.add_parser('simulate')
    simulate.add_argument("--tries", default=1000000, type=int)
    simulate.add_argument("--current_percentage", type=int)

    calculate = subparsers.add_parser('calculate')
    calculate.add_argument("--current_percentage", type=int)

    return parser.parse_args()


if __name__ == "__main__":
    arguments = parseArgs()
    #Argument verification
    if arguments.current_percentage < 0 or arguments.current_percentage > 100:
        print("The provided percentage must be between 0 and 100", file=sys.stderr)
        exit(2)
    missing_percentage = 100 - arguments.current_percentage
    if arguments.command == "simulate":
        # Argument verification
        if arguments.tries <= 0:
            if arguments.current_percentage < 0 or arguments.current_percentage > 100:
                print("The number of tries must be superior to 0", file=sys.stderr)
                exit(3)

        results = repeatAndCount(arguments.tries, SimulateN, (missing_percentage,))
        print("\nSimulation:")
        print("fails:" + str(results.get(False, 0)))
        print("success:" + str(results.get(True, 0)))
        print("total:" + str(results.get(False, 0) + results.get(True, 0)))
        print("Success ratio: " + str((results.get(True, 0) * 100) / arguments.tries) + "%")
    elif arguments.command == "calculate":
        print("Calculated chance of success: " + str(calculateChanceOfSuccess(missing_percentage) * 100) + "%")
    else:
        print("Unrecognised command:" + arguments.command, file=sys.stderr)
        exit(1)
