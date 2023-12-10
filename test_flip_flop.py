from flip_flop import FlipFlop
from logic_gate import LogicGate


def test_set_id():
    flipflop = FlipFlop("1", True, True)
    assert flipflop.id == "1"
    flipflop.id = "2"
    assert flipflop.id == "2"


def test_create_flip_flop():
    flipflop = FlipFlop("1", True, True)
    assert flipflop.value == 1
    assert flipflop._entry
    assert flipflop.id == "1"


def test_update_value():
    flipflop = FlipFlop("1", False, True)
    assert flipflop.value
    flipflop.update_value()
    assert not flipflop.value


def test_load_value():
    flipflop = FlipFlop("1", True, True)
    assert flipflop.value
    flipflop.load_value(False)
    assert not flipflop.value
