#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    lines = [int(line.rstrip()) for line in fp]

targetNumber = 167829540

start = 0
counter = 1
while True:
    mySlice = lines[start:counter]
    mySum = sum(mySlice)
    if mySum == targetNumber:
        print('XMAS encryption weakness: %d' % (min(mySlice) + max(mySlice)))
        break
    elif mySum > targetNumber:
        start += 1
        counter = start

    counter += 1