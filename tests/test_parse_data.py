import parse_data
from flip_flop import FlipFlop
from pytest import raises
from parse_data import EntryAmountError, NotAvailableTypeError
import io


# --- tests for create_logic_gate ---
def test_create_logic_gate_typical():
    flip_flops = [
        FlipFlop("1", True, True),
        FlipFlop("2", True, True),
    ]
    gate_dict = {"type": "AND", "flip-flops": [1, 2]}

    logic_gate, entries = parse_data.create_logic_gate(gate_dict, flip_flops)
    assert entries == {1, 2}
    assert logic_gate.value is True
    assert logic_gate._entries == flip_flops


def test_create_logic_gate_no_entries():
    flip_flops = [
        FlipFlop("1", True, True),
        FlipFlop("2", True, True),
    ]
    gate_dict = {"type": "AND", "flip-flops": []}
    with raises(EntryAmountError):
        parse_data.create_logic_gate(gate_dict, flip_flops)


def test_create_logic_gate_wrong_entry_type():
    flip_flops = [
        FlipFlop("1", True, True),
        FlipFlop("2", True, True),
    ]
    gate_dict = {"type": "AND", "flip-flops": "test_string"}
    with raises(TypeError):
        parse_data.create_logic_gate(gate_dict, flip_flops)


def test_create_logic_gate_type_not_supported():
    flip_flops = [
        FlipFlop("1", True, True),
        FlipFlop("2", True, True),
    ]
    gate_dict = {"type": "NONE", "flip-flops": [1]}
    with raises(NotAvailableTypeError):
        parse_data.create_logic_gate(gate_dict, flip_flops)


def test_create_logic_gate_nested():
    flip_flops = [
        FlipFlop("1", True, True),
        FlipFlop("2", True, True),
    ]
    gate_dict = {
        "type": "AND",
        "flip-flops": [1],
        "gate": {"type": "NOT", "flip-flops": [1]},
        "gate2": {"type": "NOT", "flip-flops": [2]},
    }
    logic_gate, entries = parse_data.create_logic_gate(gate_dict, flip_flops)
    assert entries == {1, 2}
    assert logic_gate.value is False


def test_create_logic_gate_nested_over_limit():
    flip_flops = [
        FlipFlop("1", True, True),
        FlipFlop("2", True, True),
    ]
    gate_dict = {
        "type": "AND",
        "flip-flops": [2],
        "gate": {
            "type": "NOT",
            "gate": {"type": "NOT", "gate": {"type": "NOT", "flip-flops": [1]}},
        },
    }
    with raises(parse_data.MaximumDepthError):
        parse_data.create_logic_gate(gate_dict, flip_flops)


def test_create_logic_gate_missing_type():
    flip_flops = [
        FlipFlop("1", True, True),
        FlipFlop("2", True, True),
    ]
    gate_dict = {"flip-flops": []}
    with raises(parse_data.IncompleteJsonError):
        parse_data.create_logic_gate(gate_dict, flip_flops)


# --- tests for flip-flop ---
def test_create_flip_flop():
    flip_flop_dict = {
        "starting-value": True,
    }
    flip_flop = parse_data.create_flip_flop("this_is_id", flip_flop_dict)
    assert flip_flop.value is True
    assert flip_flop._entry is True


def test_create_flip_flop_no_starting_value():
    flip_flop_dict = {
        "smth-smth": True,
    }
    with raises(parse_data.IncompleteJsonError):
        parse_data.create_flip_flop("this_is_id", flip_flop_dict)


def test_create_flip_flop_starting_value_not_bool():
    flip_flop_dict = {
        "starting-value": "not_a_bool",
    }
    with raises(parse_data.IncompleteJsonError):
        parse_data.create_flip_flop("this_is_id", flip_flop_dict)


# --- tests for create_register ---
def test_create_register_single_flip_flop():
    fake_json = io.StringIO(
        """
        {
            "1": {
                "starting-value": true,
                "gate": {
                    "type": "NOT",
                    "flip-flops": [1]
                }
            }
        }
        """
    )
    register = parse_data.parse_data(fake_json)
    assert len(register) == 1
    assert register.values() == [True]
    assert register.updated_values() == [False]


def test_create_register_random_json():
    fake_json = io.StringIO(
        """
        {"menu": {
                    "id": "file",
                    "value": "File",
                    "popup": {
                        "menuitem": [
                        {"value": "New", "onclick": "CreateNewDoc()"},
                        {"value": "Open", "onclick": "OpenDoc()"},
                        {"value": "Close", "onclick": "CloseDoc()"}
                        ]
                    }
                    }}
        """
    )
    with raises(parse_data.IncompleteJsonError):
        parse_data.parse_data(fake_json)
