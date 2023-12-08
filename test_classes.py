from classes import FlipFlop


def test_set_id():
    flipflop = FlipFlop("1", None, None)
    assert flipflop.id == "1"
    flipflop.id = "2"
    assert flipflop.id == "2"
