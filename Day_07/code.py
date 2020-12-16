#!/usr/bin/env python3

import re

with open('input.txt', 'r') as fp:
    rows = [line.rstrip() for line in fp]

pattern = re.compile('(.+) contain (.+)\.')

listOfBags = []
def findBags(searchTerm):
    for row in rows:
        match = pattern.match(row)
        if (None != re.search(searchTerm, match.group(2))):
            newSearchTerm = match.group(1).replace(' bags', '')
            listOfBags.append(newSearchTerm)
            findBags(newSearchTerm)

findBags('shiny gold')
print('Bags containing shiny gold bags: %d' % len(list(set(listOfBags))))
