from logic_gate import LogicGate
from flip_flop import FlipFlop


def test_create_logic_gate_AND_true():
    flip_flop = FlipFlop("1", True, True)
    logic_gate = LogicGate([flip_flop, flip_flop], "AND")
    assert logic_gate._entries == [flip_flop, flip_flop]
    assert logic_gate.value


def test_create_logic_gate_AND_false():
    flip_flop = FlipFlop("1", False, False)
    flip_flop2 = FlipFlop("2", False, False)
    logic_gate = LogicGate([flip_flop, flip_flop2], "AND")
    assert logic_gate._entries == [flip_flop, flip_flop2]
    assert not logic_gate.value


def test_create_logic_gate_OR_true():
    flip_flop = FlipFlop("1", True, True)
    logic_gate = LogicGate([flip_flop, flip_flop], "OR")
    assert logic_gate._entries == [flip_flop, flip_flop]
    assert logic_gate.value


def test_create_logic_gate_OR_false():
    flip_flop = FlipFlop("1", False, False)
    logic_gate = LogicGate([flip_flop, flip_flop], "OR")
    assert logic_gate._entries == [flip_flop, flip_flop]
    assert not logic_gate.value


def test_create_nested_logic_gate():
    flip_flop = FlipFlop("1", False, False)
    flip_flop2 = FlipFlop("2", True, True)

    logic_gate = LogicGate([flip_flop2, flip_flop, flip_flop2], "OR")
    assert logic_gate.value

    logic_gate2 = LogicGate([logic_gate, flip_flop], "AND")

    assert not logic_gate2.value
