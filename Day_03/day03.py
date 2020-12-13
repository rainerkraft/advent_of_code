#!/usr/bin/env python3

with open('input.csv') as fp:
    rows = [line.rstrip() for line in fp]

rowLength = len(rows[0])

def countTrees(rightStep, downStep):
    rowCounter = 0
    treeCounter = 0
    rowIndex = rightStep
    for row in rows:
        rowCounter += 1
        if (rowCounter <= downStep) or (downStep > 1 and (rowCounter % downStep-1) != 0): continue
        if row[rowIndex] == '#': treeCounter += 1
        nextIndex = rowIndex+rightStep
        rowIndex = nextIndex if nextIndex < rowLength else nextIndex - rowLength

    return treeCounter

routes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

totalTrees = 0
for route in routes:
    trees = countTrees(route[0], route[1])
    totalTrees = trees if totalTrees == 0 else totalTrees * trees
    print('Number of trees (Right %d, down %d):' % (route[0], route[1]), trees)

print('Total trees: %d' % totalTrees)
