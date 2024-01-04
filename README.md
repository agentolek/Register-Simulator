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
As arguments, need to give:
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

#### How to build a gate dict?
"gate" <b>must</b> contain:
- "type": for example "AND"/"OR"/"NOT"/... -> the type of the gate

The below elements are entries, each gate must contain at least 1:
- "flip-flops": [1, 2, 3] -> list of flip-flops which enter the gate. Cannot be empty.
- "gate": {gate_dict} -> gate entering the gate as input.
- "gate2", "gate3", etc... -> if more then one gate enters the current gate, name them like this in the json file. Maximum of 5 gates can be nested in one gate, so goes up to gate5.

#### Other requirements:
- At least one flip-flop must be in the json.
- One of the entries for each flip-flop must be the previous flip-flop (so 1 must enter 2, and so on.) For the first flip-flop, the last flip-flop must enter it. If there is only one flip-flop, it must enter itself.

## Output:

The program will print the first 9999 sequences created. What's more, it will create a .txt file containing the results of its labor.

Its top 2 lines will be occupied by statistics regarding your created sequences: the percentage of available unique sequences created, and the average number of bits changed between each cycle.  
Following them, each sequence which ran through the register will be written as a series of 1's and 0's. The first sequence will be the initial values of the register!

An example output file has also been included in the repo, named "test_output_file.txt."

## Classes:

<b>Register</b>:
Simulates the register, is used to generate new sequences during the program's use. Consists of a list of FlipFlops.  
<b>LogicGate</b>:
Every logic gate used in program is a member of this class. Its use is to simulate the value a real gate of given type would have, and return that value.  
<b>FlipFlop</b>:
A simulation of a type-D flip-flop. Used to get values used in generated sequences.

## Self-reflection:

The project took me more time to complete than I would have liked it to. I attribute this to one factor in particular: <ins>not planning throughly enough, rushing</ins>.  
I spent a lot of the time refactoring working code which didn't support features I needed to implement, was written in an inelegant way, or went against rules of good programming, like SOLID.  
I believe that had I taken the time to write my code well in the first place, it would have saved me hours of work. Same goes for planning.

Also, I should have been using type hints to begin with, not have added them at the end. They're pretty useful.

## Authors and acknowledgment
Created entirely by Aleksander Nowak.
I would like to thank:
- Raymund Kożuszek, for his excellent guidance and priceless advice
- And <s>not</s> Mateusz Guliński, for his mental support through these trying times.

## Project status
Complete.
