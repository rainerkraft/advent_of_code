#!/usr/bin/env python3

import itertools

with open('input.txt', 'r') as fp:
    lines = [int(line.rstrip()) for line in fp]

preamble = 25

def isValidNextNumber(nextNumber, previousInPreamble):
    combos = itertools.combinations(previousInPreamble, 2)
    for combo in combos:
        if sum(combo) == int(nextNumber):
            return True
    return False

start = 0
while True:
    if preamble + start >= len(lines):
        break
    nextNumber = lines[preamble + start]
    result = isValidNextNumber(nextNumber, lines[start:preamble + start])
    if result == False:
        print('Part 1:', nextNumber)
        break
    start += 1
