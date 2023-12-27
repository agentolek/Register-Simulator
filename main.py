import argparse
import sys
from parse_data import parse_data


def parse_terminal_input(arguments):
    parser = argparse.ArgumentParser()

    parser.add_argument("json_path")
    parser.add_argument("destination_path")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--steps")
    group.add_argument("--until-loop", action="store_true")

    return parser.parse_args(arguments[1:])


def main(arguments):
    args = parse_terminal_input(arguments)
    print(args)


if __name__ == "__main__":
    main(sys.argv)
