import json
from flip_flop import FlipFlop
from logic_gate import LogicGate, EntryAmountError
from register import Register


MAXIMUM_NESTED_GATES: int = 5


class IncompleteJsonError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("The json file is missing something!")


def read_from_json(file_handle):
    data = None
    try:
        data = json.load(file_handle)
    except json.JSONDecodeError:
        # FIXME: wrong error used
        raise IncompleteJsonError
    return data


def create_flip_flop(id, flip_flop):
    starting_value = flip_flop.get("starting-value", None)
    if starting_value is None:
        raise IncompleteJsonError(flip_flop)
    if not isinstance(starting_value, bool):
        raise IncompleteJsonError(flip_flop)

    return FlipFlop(id, starting_value, starting_value)


def create_logic_gate(logic_gate: dict, flip_flops: list):
    flip_flops_entering = []
    entries = []
    # FIXME: add limit to level of nesting, catch errors like flipflop
    # id out of range
    if "type" not in logic_gate:
        raise IncompleteJsonError(logic_gate)

    if not ("flip-flops" in logic_gate or "gate" in logic_gate):
        raise IncompleteJsonError(logic_gate)

    if "flip-flops" in logic_gate:
        flip_flops_entering += logic_gate["flip-flops"]
        entries += [flip_flops[id - 1] for id in logic_gate["flip-flops"]]

    if "gate" in logic_gate:
        gate_result = create_logic_gate(logic_gate.get("gate"), flip_flops)
        entries += [gate_result[0]]
        flip_flops_entering += gate_result[1]

    for counter in map(str, range(2, MAXIMUM_NESTED_GATES + 1)):
        if ("gate" + counter) in logic_gate:
            gate_result = create_logic_gate(logic_gate.get("gate"), flip_flops)
            entries += [gate_result[0]]
            flip_flops_entering += gate_result[1]
        else:
            break

    return LogicGate(entries, logic_gate["type"]), flip_flops_entering


def create_register(data):
    flip_flops: list[FlipFlop] = []

    # this part creates base FlipFlops
    for id in data:
        flip_flop = data.get(id)
        flip_flops.append(create_flip_flop(id, flip_flop))

    # this part sets the entries of the FlipFlops created
    # above to be LogicGate/previous FlipFlop
    counter = 0
    for id in data:
        flip_flop = data.get(id)
        gate = flip_flop.get("gate", None)
        if gate:
            gate_result = create_logic_gate(gate, flip_flops)

            # these ifs check if previous flip_flop is one of the entries for
            # current one
            if counter and counter not in gate_result[1]:
                raise IncompleteJsonError(gate)
            elif len(flip_flops) not in gate_result[1]:
                raise IncompleteJsonError(gate)

            flip_flops[counter].set_entry(gate_result[0])
        else:
            flip_flops[counter].set_entry(flip_flops[counter - 1])

        counter += 1

    return Register(flip_flops)


def parse_data(path):
    data = None
    # TODO: catch errors like NotAFile, NoFile, etc
    with open(path, "r") as f:
        data = read_from_json(f)

    register = create_register(data)

    return data


if __name__ == "__main__":
    data = parse_data("test_input_file.json")
    pass
