#!/usr/bin/env python3

with open('input.csv') as fp:
    rows = [line.rstrip() for line in fp]

length = len(rows[0])

rowCounter = 0
treeCounter = 0
rowIndex = 1
rightStep = 1
downStep = 2
for row in rows[::downStep]:
    rowCounter += downStep
    if rowCounter <= downStep: continue
    treeCounter += 1 if row[rowIndex] == '#' else 0
    nextIndex = rowIndex+rightStep
    rowIndex = nextIndex if nextIndex < length else nextIndex - length

print('Number of trees (Right %d, down %d):' % (rightStep, downStep), treeCounter)
