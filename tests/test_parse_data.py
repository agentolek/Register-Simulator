import parse_data
from flip_flop import FlipFlop


def test_create_logic_gate_typical():
    flip_flops = [
        FlipFlop("1", True, True),
        FlipFlop("2", True, True),
    ]
    gate_dict = {"type": "AND", "flip-flops": [1, 2]}

    logic_gate, entries = parse_data.create_logic_gate(gate_dict, flip_flops)
    assert entries == [1, 2]
    assert logic_gate.value is True
    assert logic_gate._entries == flip_flops
