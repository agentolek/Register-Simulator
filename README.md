# Rejestr - PiPR Project

## Name
A model of a register created using flip-flops, made in Python. 

## Description
Current plans for design:

Parse input (ensure it's correct, then convert it to usable stuff), take a .txt file or smth:
- number of flip-flops
- number of steps taken
- number until loop (return to starting value)
- logic gates on each flip-flop
- starting word (set of bits)

How stuff works:
class logic gate -> - type of gate as str, np. "OR", "AND"
                    - entry points of gate, which can be other gates, flip-flops, or bools
                    - property value -> returns the caluculated value based on type of gate
class flip-flop -> contains:
                    - logic-gate/flip-flip/bool entering it as input value (bool only for testing purposes)
                    - property value -> updates_value, returns the value of thing on input
                    - property id -> returns id <mark>this could be useless</mark>
                    - ???
class register -> contains:
                    - length = number of flip-flops in it
                    - table of flip-flop objects of "length" length
                    - .values() method, which returns the values of all flip-flops
                    - .value() methos, which returns the value of a single flip-flop

Output:
stopień wykorzystania przestrzeni (szereg N przerzutników hipotetycznie daje 2^N kombinacji a ile zostało wygenerowanych)
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
