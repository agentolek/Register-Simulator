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
class logic gate -> all logic gates have only 2 entry points, more entry points = compound gate?,
                    or do some magic math to make them work for infinite gates like, multiplication for AND gate
                    also contain logic gates leading into them
class flip-flop -> contains:
                    - logic gate entering it (there can only be one, defaults to or with logic gate/previous
                    - exit value?
                    - id (number in output)
                    - ???

Output:
stopień wykorzystania przestrzeni (szereg N przerzutników hipotetycznie daje 2^N kombinacji a ile zostało wygenerowanych)
różnorodność ciągu - średnia liczba bitów różniących się pomiędzy wyrazami ciągu.
created words of n length

Possible issues:
when doing "until loop" can enter a loop which doesn't return you to starting value
                    
## Authors and acknowledgment
Aleksander Nowak, and i would like to thank:
- me
- myself
- I
for all of their hard work.

## Project status
In development.
