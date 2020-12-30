#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    lines = [int(line.rstrip()) for line in fp]

lookup = {
    0: 1,
    1: 1,
    2: 1,
    3: 2,
    4: 4,
    5: 7,
    6: 12,
    7: 20,
    8: 33,
    9: 54,
    10: 88
}

sortedJoltages = sorted(lines)
sortedJoltages.append(max(lines) + 3)
if sortedJoltages[0] != 0:
    sortedJoltages.insert(0, 0)

result = 1
prevJoltage = 0
consecutiveCounter = 0
for joltage in sortedJoltages:
    consecutiveCounter += 1
    if joltage != prevJoltage + 1:
        result = lookup[consecutiveCounter] * result
        consecutiveCounter = 0
    prevJoltage = joltage

print('RESULT:', result)
