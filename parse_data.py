import json
from flip_flop import FlipFlop
from logic_gate import LogicGate
from register import Register


MAXIMUM_GATES_IN_GATE: int = 5
MAXIMUM_GATE_DEPTH: int = 3


class IncompleteJsonError(Exception):
    pass


class MaximumDepthError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(
            f"Your gate exceeeded the maximum depth limit of {MAXIMUM_GATE_DEPTH}"
        )


def read_from_json(file_handle):
    # data = None
    # try:
    #     data = json.load(file_handle)
    # except json.JSONDecodeError:
    #     raise json.JSONDecodeError("Json provided is not formatted properly!")
    # return data
    return json.load(file_handle)


def create_flip_flop(id, flip_flop):
    """
    Returns flip-flop without proper input,
    temporarily putting a bool in its place.
    """
    starting_value = flip_flop.get("starting-value", None)
    if starting_value is None:
        raise IncompleteJsonError(
            f"Your flip_flop named '{id}' is missing starting-value!"
        )
    if not isinstance(starting_value, bool):
        raise IncompleteJsonError(
            f"The starting value of your flip_flop named '{id}' is not a bool!"
        )

    return FlipFlop(id, starting_value, starting_value)


def create_logic_gate(logic_gate: dict, flip_flops: list, depth=0):
    """
    Given a gate dict and list of flip-flops,
    creates and returns a LogicGate object and list of flip-flops entering it.

    Works with nested gates.
    """
    flip_flops_entering = []
    entries = []

    # limits the level of nesting a gate can have
    if depth >= 3:
        raise MaximumDepthError(logic_gate)

    # check for mandatory keys in dict
    if "type" not in logic_gate or (
        not ("flip-flops" in logic_gate or "gate" in logic_gate)
    ):
        raise IncompleteJsonError("This logic gate is missing an entry: ", logic_gate)

    # adds flip-flops to entry list
    if "flip-flops" in logic_gate:
        flip_flops_entering += logic_gate["flip-flops"]
        try:
            entries += [flip_flops[id - 1] for id in logic_gate["flip-flops"]]
        except IndexError:
            raise IncompleteJsonError(
                "FlipFlop number is out of range in gate: ", logic_gate
            )

    # creates nested gates and adds them to entries,
    # also adds its entries to entry list
    for counter in map(str, [""] + list(range(2, MAXIMUM_GATES_IN_GATE + 1))):
        if ("gate" + counter) in logic_gate:
            gate_result = create_logic_gate(
                logic_gate.get("gate" + counter), flip_flops, depth + 1
            )
            entries += [gate_result[0]]
            flip_flops_entering += gate_result[1]
        else:
            break

    return LogicGate(entries, logic_gate["type"]), set(flip_flops_entering)


def create_register(data):
    """
    Given a properly formatted json file, this function will turn it
    into a member of the class Register.
    """
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
            # current one, separate ifs for first flip-flop and all others
            if counter == 0 and len(flip_flops) not in gate_result[1]:
                raise IncompleteJsonError(
                    f"Previous flip_flop does not enter flip_flop named {id}",
                    gate_result[0],
                )
            elif counter != 0 and counter not in gate_result[1]:
                raise IncompleteJsonError(
                    f"Previous flip_flop does not enter flip_flop named {id}",
                    gate_result[0],
                )

            flip_flops[counter].set_entry(gate_result[0])
        else:
            flip_flops[counter].set_entry(flip_flops[counter - 1])

        counter += 1

    return Register(flip_flops)


def parse_data(file_handle):
    data = read_from_json(file_handle)

    register = create_register(data)

    return register
