# Rejestr - PiPR Project

## Description
A model of a register created using type D flip-flops, made in Python.

<b>The available types of gates are:</b>
- NOT - max 1 entry
- AND - unlimited entries
- OR - unlimited entries
- NAND - unlimited entries
- NOR - unlimited entries

## How it works:

Activate program using terminal.
Need to give:
- path of .json file containing register configuration data
- path to file the program will write its output to

Either one of the below flags must be present:
- --until-loop -> the program will work until it creates an already generated sequence
- --steps :int: -> the program will generate a certain number of sequences.

### What does the input json need to look like?

An example input file has been included in the repo, named "test_input_file.json."
The base dicts should be named after numbers from 1 to N (but don't have to), where N is the number of flip-flops. These dicts will represent your flip-flops. They will be added to the register in the order they are given.

Each of these dicts <b>must</b> consist of these elements:
- "starting-value": true/false -> the initial value of the flip-flop

They can also contain the following elements:
- "gate" (dict, description below) -> the gate serving as the flip-flops input.

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

## Output:

The program will print the first 9999 sequences created. What's more, it will create a .txt file containing the resulsts of its hard labor.

Its top 2 lines will be occupied by statistics regarding your created sequences: the percentage of available unique sequences created, and the average number of bits changed between each cycle.

Following them, each sequence which ran through the register will be written as a series of 1's and 0's. The first sequence will be the initial values of the register!!!

An example output file has also been included in the repo, named "test_output_file.txt."

## Authors and acknowledgment
Created entirely by Aleksander Nowak.

I would like to thank:
- Raymund Kożuszek, for his excellent guidance and priceless advice
- And <s>not</s> Mateusz Guliński, for his mental support through these trying times.

## Project status
Almost done?
