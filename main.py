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
    parser = argparse.ArgumentParser(prog="main.py")

    parser.add_argument("json_path", help="Path to input json.")
    parser.add_argument("destination_path", help="Path to output txt file.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--steps",
        type=int,
        help="Specifies that the program should generate STEPS new sequences.",
    )
    group.add_argument(
        "--until-loop",
        action="store_true",
        help="Specifies that the program should generate sequences until it creates an already acquired sequence.",
    )

    args = parser.parse_args(arguments[1:])

    if args.steps <= 0:
        raise StepError

    return args


def visualise_sequence(sequence, seq_number):
    """
    Prints the generated sequence in terminal.
    """
    # Program only visualises the first 9999 sequences created.
    if seq_number > 10000:
        return

    print_string = str(seq_number - 1) + ". "
    print_string = print_string.zfill(6)
    for elem in sequence:
        if elem:
            # uses an em dash which isn't in ASCII,
            # so might not work everywhere
            print_string += "—"
        else:
            print_string += "_"
    print(print_string)


def run_register(register: Register, steps: int = None, looped=False):
    """
    Runs the register, creating new sequences and returning a list of sequences
    created.

    If looped == True, new sequences will stop being generated once
    a sequence is repeated.
    If steps != None, X new sequences will be generated, with X being
    the integer passes as steps.
    """
    created_sequences = []
    max_counter = steps + 1 if steps else -1

    while max_counter != 0:
        current_values = tuple(register.values())

        if (current_values in created_sequences) and looped:
            created_sequences.append(current_values)
            visualise_sequence(current_values, len(created_sequences))
            break

        created_sequences.append(current_values)
        visualise_sequence(current_values, len(created_sequences))
        register.update()
        max_counter -= 1

    return created_sequences


def calc_utilization_rate(created_sequences, register):
    """
    Calculates the percentage of available sequences that were created
    using program.
    """
    return round(len(set(created_sequences)) / (2 ** len(register)), 4)


def calc_avg_bit_difference(created_sequences, register):
    """
    Calculates the average difference between sequences created using program.
    """
    bits_differing = []
    for i in range(1, len(created_sequences)):
        prev_sequence = created_sequences[i - 1]
        curr_sequence = created_sequences[i]
        diff_counter = 0

        for c in range(len(register)):
            if prev_sequence[c] != curr_sequence[c]:
                diff_counter += 1

        bits_differing.append(diff_counter)

    return round((sum(bits_differing) / len(bits_differing)), 2)


def write_to_file(write_file_path, sequences, utilization_rate, avg_diff):
    try:
        with open(write_file_path, "w") as f:
            f.write(
                f"Percentage of possible seqences created: {utilization_rate*100}%\n"
            )
            f.write(f"Average number of bits changed between sequences: {avg_diff}\n")
            for sequence in sequences:
                write_string = "".join(["1" if value else "0" for value in sequence])
                f.write(f"{write_string}\n")
    except Exception:
        print("Couldn't write to file, something is wrong with path given!!!")


def get_register(path):
    try:
        with open(path, "r") as f:
            return parse_data(f)
    except FileNotFoundError:
        raise FileNotFoundError("Path to input json doesn't point to a file!")


def main(arguments):
    args = parse_terminal_input(arguments)
    created_sequences = []

    register = get_register(args.json_path)

    created_sequences = run_register(register, args.steps, args.until_loop)

    util_rate = calc_utilization_rate(created_sequences, register)
    avg_diff = calc_avg_bit_difference(created_sequences, register)

    write_to_file(args.destination_path, created_sequences, util_rate, avg_diff)


if __name__ == "__main__":
    main(sys.argv)
