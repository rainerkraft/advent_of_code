#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    seatplan = [line.rstrip() for line in fp]

def howManyOccupied(rowNum, seatNum, rowRight, seatplanDown):
    numOccupiedSeats = 0
    if seatNum > 0:
        if seatplan[rowNum][seatNum - 1] == '#':
            numOccupiedSeats += 1
    if seatNum < rowRight:
        if seatplan[rowNum][seatNum + 1] == '#':
            numOccupiedSeats += 1
    if rowNum > 0:
        if seatNum > 0:
            if seatplan[rowNum - 1][seatNum - 1] == '#':
                numOccupiedSeats += 1
        if seatplan[rowNum - 1][seatNum] == '#':
            numOccupiedSeats += 1
        if seatNum < rowRight:
            if seatplan[rowNum - 1][seatNum + 1] == '#':
                numOccupiedSeats += 1
    if rowNum < seatplanDown:
        if seatNum > 0:
            if seatplan[rowNum + 1][seatNum - 1] == '#':
                numOccupiedSeats += 1
        if seatplan[rowNum + 1][seatNum] == '#':
            numOccupiedSeats += 1
        if seatNum < rowRight:
            if seatplan[rowNum + 1][seatNum + 1] == '#':
                numOccupiedSeats += 1
    
    return numOccupiedSeats

filledSeats = 0
def fillSeats(mySeatplan):
    global filledSeats
    newSeatplan = [''] * len(mySeatplan)
    rowNum = 0
    seatplanDown = len(mySeatplan) - 1
    for rowString in mySeatplan:
        row = list(rowString)
        rowRight = len(row) - 1
        seatNum = -1
        for seat in row:
            seatNum += 1
            if '.' != seat:
                occupied = howManyOccupied(rowNum, seatNum, rowRight, seatplanDown)
                if 'L' == seat and occupied == 0:
                    row[seatNum] = '#'
                    filledSeats += 1
                elif '#' == seat and occupied >= 4:
                    row[seatNum] = 'L'
                    filledSeats -= 1
            newRow = "".join(row)
            newSeatplan[rowNum] = newRow
        rowNum += 1
    
    return newSeatplan

prevSeatplan = [''] * len(seatplan)
while prevSeatplan != seatplan:
    prevSeatplan = seatplan
    seatplan = fillSeats(seatplan)

print('Occupied seats', "".join(seatplan).count('#'))
