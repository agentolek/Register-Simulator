import argparse
import sys
from parse_data import parse_data
from register import Register


class StepError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Number of steps must be greater than 0!")


def parse_terminal_input(arguments):
    """
    Parses flags and argments typed in terminal into usable data.
    Also checks if all of the necessary arguments are there.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("json_path")
    parser.add_argument("destination_path")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--steps")
    group.add_argument("--until-loop", action="store_true")

    return parser.parse_args(arguments[1:])


def visualise_sequence(sequence, seq_number):
    """
    Prints the generated sequence in terminal.
    """
    print_string = str(seq_number) + ". "
    for elem in sequence:
        if elem:
            print_string += "-"
        else:
            print_string += "_"
    print(print_string)


# TODO: maybe refactor run_for_steps and run_until_loop into one function?
def run_for_steps(register: Register, steps: int):
    """
    Creates X new sequences from register, where X is the number of steps.
    Returns the sequences created.
    """
    created_sequences = []

    for _ in range(steps):
        current_values = register.values()
        visualise_sequence(current_values, len(created_sequences))
        created_sequences.append(current_values)
        register.update()

    return created_sequences


def run_until_loop(register: Register):
    """
    Creates new sequences from given register until it hits a loop.
    Returns the sequences created.
    """
    created_sequences = []

    while True:
        current_values = register.values()

        if current_values in created_sequences:
            created_sequences.append(current_values)
            visualise_sequence(current_values, len(created_sequences))
            break

        created_sequences.append(current_values)
        visualise_sequence(current_values, len(created_sequences))
        register.update()

    return created_sequences


def main(arguments):
    args = parse_terminal_input(arguments)
    created_sequences = []

    register = parse_data(args.json_path)
    if args.steps:
        if args.steps <= 0:
            raise StepError

    if args.until_loop:
        created_sequences = run_until_loop(register)
    else:
        created_sequences = run_for_steps(register, args.steps)


if __name__ == "__main__":
    main(sys.argv)
