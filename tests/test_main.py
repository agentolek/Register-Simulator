import main
from register import Register
from parse_data import parse_data
from pytest import approx, raises
import sys
import io


def test_calc_utilization_rate():
    util_rate = main.calc_utilization_rate(
        [(True, False), (True, True), (False, True)], Register(["a", "b"])
    )
    assert util_rate == approx(0.75)


def test_calc_avg_bit_difference():
    bit_diff = main.calc_avg_bit_difference(
        [(True, False), (False, True), (True, False)], Register(["a", "b"])
    )
    assert bit_diff == approx(2)


def test_parse_terminal_input():
    test_args = [
        "/home/agentolek/rejestr-pipr-projekt/main.py",
        "./tests/test_input_file.json",
        "./tests/test_output_file.txt",
        "--steps",
        "12",
    ]
    args = main.parse_terminal_input(test_args)

    assert args.json_path == "./tests/test_input_file.json"
    assert args.destination_path == "./tests/test_output_file.txt"
    assert args.steps == 12


def test_parse_terminal_input_negative_steps():
    test_args = [
        "/home/agentolek/rejestr-pipr-projekt/main.py",
        "./tests/test_input_file.json",
        "./tests/test_output_file.txt",
        "--steps",
        "-5",
    ]
    with raises(main.StepError):
        main.parse_terminal_input(test_args)


def test_visualise_sequences():
    capturedPrint = io.StringIO()
    sys.stdout = capturedPrint
    main.visualise_sequences([[True, False], [False, False], [True, True]])
    assert capturedPrint.getvalue() == "1: 101\n2: 001\n"


def test_run_register_typical():
    register = main.get_register("tests/example_input_file.json")
    sequences = main.run_register(register, 3)
    assert sequences == [
        (True, False, True),
        (False, True, True),
        (True, False, True),
        (False, True, True),
    ]

    sequences = main.run_register(register, looped=True)
    assert sequences == [
        (True, False, True),
        (False, True, True),
        (True, False, True),
    ]


def test_run_register_single_flip_flop():
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
    register = parse_data(fake_json)
    sequences = main.run_register(register, 3)
    assert sequences == [(True,), (False,), (True,), (False,)]

    sequences = main.run_register(register, looped=True)
    assert sequences == [(True,), (False,), (True,)]
