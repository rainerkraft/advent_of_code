#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    directions = [line.rstrip() for line in fp]

compassPoints = ['E', 'S', 'W', 'N']
lenCompassPoints = len(compassPoints)
journey = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
facing = 'E'
for direction in directions:
    whereTo = direction[:1]
    paces = int(direction[1:])

    if 'F' == whereTo:
        journey[facing] += paces
        continue
    if 'R' == whereTo:
        turnTo = compassPoints.index(facing) + int(paces/90)
        if turnTo > lenCompassPoints - 1:
            turnTo -= lenCompassPoints
        facing = compassPoints[turnTo]
        continue
    if 'L' == whereTo:
        turnTo = compassPoints.index(facing) - int(paces/90)
        if turnTo < 0:
            turnTo += lenCompassPoints
        facing = compassPoints[turnTo]
        continue

    journey[whereTo] += paces


result = abs(journey['E'] - journey['W']) + abs(journey['S'] - journey['N'])

print('Manhattan distance:', result)