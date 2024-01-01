import json
from flip_flop import FlipFlop
from logic_gate import LogicGate
from register import Register


MAXIMUM_GATES_IN_GATE: int = 5
MAXIMUM_GATE_DEPTH: int = 3


class IncompleteJsonError(Exception):
    pass


class MaximumDepthError(Exception):
    def __init__(self, id) -> None:
        super().__init__(
            f"Gate exceeded the maximum depth limit of {MAXIMUM_GATE_DEPTH} in flip-flop '{id}'!"
        )


class NotAvailableTypeError(Exception):
    def __init__(self, id, type_) -> None:
        super().__init__(
            f"A gate in flip-flop '{id}' is using unsupported type {type_}!"
        )


class EntryAmountError(Exception):
    def __init__(self, id, type_) -> None:
        super().__init__(
            f"A gate, type {type_}, in flip_flop '{id}' isn't using proper nr of entries!"
        )


def read_from_json(file_handle):
    return json.load(file_handle)


def create_flip_flop(id: str, flip_flop: dict):
    """
    Returns flip-flop without proper input,
    temporarily putting a bool in its place.
    """
    starting_value = flip_flop.get("starting-value", None)
    if starting_value is None:
        raise IncompleteJsonError(f"Your flip_flop '{id}' is missing starting-value!")
    if not isinstance(starting_value, bool):
        raise IncompleteJsonError(
            f"The starting value of your flip_flop '{id}' is not a bool!"
        )

    return FlipFlop(id, starting_value, starting_value)


def check_gate(logic_gate: dict, entries: list, id: str, depth: int):
    """
    Runs tests to see if a LogicGate object can be created using given data.
    """
    # limits the level of nesting a gate can have
    if depth >= 3:
        raise MaximumDepthError(id)

    # check for mandatory keys in dict
    if "type" not in logic_gate:
        raise IncompleteJsonError(f"A gate has no type in flip-flop '{id}'!")

    if not ("flip-flops" in logic_gate or "gate" in logic_gate):
        raise IncompleteJsonError(
            f"A gate, type {logic_gate['type']} has no entries in flip-flop '{id}'!"
        )

    # checks if type is supported
    if logic_gate["type"] not in LogicGate.AVAILABLE_TYPES:
        raise NotAvailableTypeError(id, logic_gate["type"])

    # checks whether number of entries is legal
    if (logic_gate["type"] == "NOT" and len(entries) != 1) or len(entries) == 0:
        raise EntryAmountError(id, logic_gate["type"])


def create_logic_gate(
    logic_gate: dict, flip_flops: list, id: str = None, depth: int = 0
):
    """
    Given a gate dict and list of flip-flops,
    creates and returns a LogicGate object and list of flip-flops entering it.
    Id is given for the purpose of writing more precise error messages.
    Depth limits depth of recursion.

    Works with nested gates.
    """
    flip_flops_entering = []
    entries = []

    # adds flip-flops to entry list
    if "flip-flops" in logic_gate:
        flip_flops_entering += logic_gate["flip-flops"]
        try:
            entries += [flip_flops[id - 1] for id in logic_gate["flip-flops"]]
        except IndexError:
            raise IndexError(
                f"Attempted use of non-existent flip-flop in flip-flop '{id}'!"
            )

    # creates nested gates and adds them to entries,
    # also adds its entries to entry list
    for counter in map(str, [""] + list(range(2, MAXIMUM_GATES_IN_GATE + 1))):
        if ("gate" + counter) in logic_gate:
            gate_result = create_logic_gate(
                logic_gate.get("gate" + counter), flip_flops, id, depth + 1
            )
            entries += [gate_result[0]]
            flip_flops_entering += gate_result[1]
        else:
            break

    check_gate(logic_gate, entries, id, depth)

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
            gate_result = create_logic_gate(gate, flip_flops, id)

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
