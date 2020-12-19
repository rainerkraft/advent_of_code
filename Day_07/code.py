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

numBags = 0
def countBags(start, prevCount):
    global numBags
    global counter
    for row in rows:
        match = pattern.match(row)
        if None != re.search(start, match.group(1)):
            allContainedBags = match.group(2)
            bags = allContainedBags.split(',')
            for bag in bags:
                bag = bag.strip()
                numSearch = re.search('\d+', bag)
                number = 0 if None == numSearch else int(numSearch[0])
                if number > 0:
                    nextStart = bag.replace(' bags', '')
                    nextStart = re.sub('\d+', '', nextStart).strip()
                    toAdd = (int(prevCount) * number)
                    numBags += toAdd
                    countBags(nextStart, toAdd)

countBags('shiny gold', 1)
print('Bags contained in shiny gold bag: %d' % numBags)
