#!/usr/bin/env python3

import itertools

with open('input.txt', 'r') as fp:
    lines = [int(line.rstrip()) for line in fp]

maxJoltage = max(lines) + 3
sortedJoltages = sorted(lines)
sortedJoltages.append(maxJoltage)

previousJoltage = 0
numDiff1 = 0
numDiff3 = 0
for joltage in sortedJoltages:
    if joltage == previousJoltage + 1:
        numDiff1 += 1
    elif joltage == previousJoltage + 3:
        numDiff3 += 1

    previousJoltage = joltage

print('Result:', numDiff1 * numDiff3)
