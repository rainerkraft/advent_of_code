#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    input = {int(timestamp.rstrip()):buslines.rstrip().split(',') for timestamp, buslines in zip(fp, fp)}

timestamp = list(input.keys())[0]
buslines = list(map(lambda line: int(line), filter(lambda line: line != 'x', input.get(timestamp))))

nearestTimes = {}
for line in buslines:
    nearestTimes[line] = (line - (timestamp % line))

nextBus = min(nearestTimes, key=nearestTimes.get)

print('Result:', nextBus * nearestTimes[nextBus])