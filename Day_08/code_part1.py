#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    lines = [line.rstrip() for line in fp]

counts = [0] * len(lines)

accumulator = 0
index = 0
while True:
    [instruction, value] = lines[index].split(' ')
    if (counts[index] > 0):
        print('Accumulator:', accumulator)
        break

    counts[index] += 1

    if (instruction == 'acc'):
        accumulator += int(value)
        index += 1
    elif (instruction == 'jmp'):
        index += int(value)
    else:
        index += 1
