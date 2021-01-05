#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    directions = [line.rstrip() for line in fp]

waypoint = {'X': 10, 'Y': 1}
ship = {'X': 0, 'Y': 0}

for direction in directions:
    instruction = direction[:1]
    value = int(direction[1:])

    if 'F' == instruction:
        ship['X'] = ship['X'] + waypoint['X'] * value
        ship['Y'] = ship['Y'] + waypoint['Y'] * value
        
    if 'R' == instruction:
        if 90 == value:
            y = waypoint['Y']
            waypoint['Y'] = waypoint['X'] * -1
            waypoint['X'] = y
        if 180 == value:
            waypoint['Y'] = waypoint['Y'] * -1
            waypoint['X'] = waypoint['X'] * -1
        if 270 == value:
            y = waypoint['Y']
            waypoint['Y'] = waypoint['X']
            waypoint['X'] = y * -1

    if 'L' == instruction:
        if 90 == value:
            y = waypoint['Y']
            waypoint['Y'] = waypoint['X']
            waypoint['X'] = y * -1
        if 180 == value:
            waypoint['Y'] = waypoint['Y'] * -1
            waypoint['X'] = waypoint['X'] * -1
        if 270 == value:
            y = waypoint['Y']
            waypoint['Y'] = waypoint['X'] * -1
            waypoint['X'] = y

    if 'N' == instruction:
        waypoint['Y'] += value
    if 'S' == instruction:
        waypoint['Y'] -= value
    if 'E' == instruction:
        waypoint['X'] += value
    if 'W' == instruction:
        waypoint['X'] -= value

print('Manhattan distance:', abs(ship['X']) + abs(ship['Y']))
