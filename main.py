import argparse
import sys
from parse_data import parse_data
from register import Register


def parse_terminal_input(arguments):
    parser = argparse.ArgumentParser()

    parser.add_argument("json_path")
    parser.add_argument("destination_path")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--steps")
    group.add_argument("--until-loop", action="store_true")

    return parser.parse_args(arguments[1:])


def run_until_loop(register: Register):
    created_sequences = []
    while True:
        current_values = register.values
        if current_values in created_sequences:
            break
        created_sequences.append(current_values)
        # TODO: resume working here


def main(arguments):
    args = parse_terminal_input(arguments)

    register = parse_data(args.json_path)

    if args.until_loop:
        run_until_loop(register)


if __name__ == "__main__":
    main(sys.argv)
