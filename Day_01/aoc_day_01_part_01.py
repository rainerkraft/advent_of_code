#!/usr/bin/env python3

import itertools

with open('input.csv') as fp:
    expenses = [int(line.rstrip()) for line in fp]

thingsPart1 = itertools.combinations(expenses, 2)

for thing in thingsPart1:
    mySum = sum(thing)
    if mySum == 2020:
        print(mySum, thing, (lambda x: x[0]*x[1])(thing))

thingsPart2 = itertools.combinations(expenses, 3)

for thing in thingsPart2:
    mySum = sum(thing)
    if mySum == 2020:
        print(mySum, thing, (lambda x: x[0]*x[1]*x[2])(thing))
