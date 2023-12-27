# Rejestr - PiPR Project

## Description
A model of a register created using flip-flops, made in Python.

## How it works:
Current plans for design:

### Input parsing:

Activate program using terminal.
Need to give:
- path of .json file containing register config stuff
- path to file te program will write its output to
And one of the below (or maybe just disregard the first one if loop flag is given, need to read docs):
Either one of the below flags must be present:
- --until-loop -> the program will work until it creates an already acquired sequence
- --steps :int: -> the program will generate a certain number of sequences.


#### What does the input json need to look like?

An example input file has been included in the repo, named "test_input_file.json."
The base dicts should be named after numbers from 1 to N, where N is the number of flip-flops. These dicts will represent your flip-flops. They will be added to the register in the order they are given.

Each of these dicts <b>must</b> consist of these elements:
- "starting-value": true/false -> the initial value of the flip-flop

They can also contain the following elements:
- "gate" (description below) -> the gate serving as the flip-flops input.
If "gate" element is not provided, then the flip-flops entry defaults to the previous flip-flop.

"gate" must contain:
- "type": for example "AND"/"OR"/"NOT"/... -> the type of the gate
The below elements are entries, each gate must contain at least 1:
- "flip-flops": [1, 2, 3] -> list of flip-flops which enter the gate
- "gate": {dict with gate stuff} -> gate entering the gate as input.
- "gate2", "gate3", etc... -> if more then one gate enters the current gate, name them like this in the json file. Maximum of 5 gates can be nested in one gate, so goes up to gate5.

Requirements:
- At least one flip-flop must be in the dict.
- One of the entries for each flip-flop must be the previous flip-flop (so 1 must enter 2, and so on.) For the first flip-flop, the last flip-flop must enter it. If there is only one flip-flop, it must enter itself.


### Classes

Class LogicGate -> contains:
- type of gate as str, np. "OR", "AND"
- entry points of gate, which can be other gates or flip-flops. Each gate must have at least one entry,
with the NOT gate also being limited to max 1 gate.
- property value -> returns the caluculated value based on type of gate

Class FlipFlop -> contains:
- logic-gate/flip-flop/bool entering it as input value (bool only for testing purposes)
- property value -> updates the value of the register based on the current input, then returns new value as bool.
- property id -> returns id <mark>this could be useless</mark>
- .update_value() method -> updates the value of the flip-flop to match the current input
- .load_value() method -> loads new value into flip-flop, regardless of what input is.

Class Register -> contains:
- __len__ = number of flip-flops in it
- flip-flops = table of flip-flop objects of "length" length
- .values() method, which returns the values of all flip-flops
- .value_of_index(index) method, which returns the value of a single flip-flop
- .update(values<list[bool]>) method, which updates the values of each flip-flop in the register to match the ones given as argmuent

Output:

stopień wykorzystania przestrzeni
(szereg N przerzutników hipotetycznie daje 2^N kombinacji a ile zostało wygenerowanych)

różnorodność ciągu - średnia liczba bitów różniących się pomiędzy wyrazami ciągu.
created words of n length

Possible bugs:
when doing "until loop" can enter a loop which doesn't return you to starting value

## Authors and acknowledgment
Aleksander Nowak, and i would like to thank:
- me
- myself
- I
for all of their hard work.

And not Mateusz Guliński, for his mental support through these trying times.

## Project status
In development.
