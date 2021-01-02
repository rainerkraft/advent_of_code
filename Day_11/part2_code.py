#!/usr/bin/env python3

import sys

with open('input.txt', 'r') as fp:
    seatplan = [line.rstrip() for line in fp]

seatplanDown = len(seatplan)
rowRight = len(seatplan[0])

def look(rowNum, seatNum):
    try:
        if seatplan[rowNum][seatNum] == 'L':
            return -1
        if seatplan[rowNum][seatNum] == '#':
            return 1
    except IndexError as ex:
        print('ROWS   :', seatplanDown)
        print('COLUMNS:', rowRight)
        print('ROWNUM :', rowNum)
        print('SEATNUM:', seatNum)
        sys.exit(ex)

    return 0

def lookHorizontal(myRange, rowNum):
    seatsSeen = 0
    for i in myRange:
        occSeats = look(rowNum, i)
        if (occSeats == -1): break
        if (occSeats > 0):
            seatsSeen += occSeats
            break

    return seatsSeen

def lookVertical(myRange, seatNum):
    seatsSeen = 0
    for i in myRange:
        occSeats = look(i, seatNum)
        if (occSeats == -1): break
        if (occSeats > 0):
            seatsSeen += occSeats
            break

    return seatsSeen

def lookDiagonal(myRange, seatNum, direction):
    originalDirection = direction
    seatsSeen = 0
    for i in myRange:
        whichSeat = seatNum + direction
        if (whichSeat >= rowRight): break
        if (whichSeat < 0): break
        occSeats = look(i, whichSeat)
        if (occSeats == -1): break
        if (occSeats > 0):
            seatsSeen += occSeats
            break
        direction += originalDirection

    return seatsSeen

def howManyOccupied(rowNum, seatNum):
    numOccupiedSeats = 0
    # LOOK WEST
    if seatNum > 0:
        numOccupiedSeats += lookHorizontal(range(seatNum - 1, -1, -1), rowNum)

    # LOOK EAST
    if seatNum < rowRight:
        numOccupiedSeats += lookHorizontal(range(seatNum + 1, rowRight, 1), rowNum)

    # UP
    if rowNum > 0:
        # LOOK NORTH
        numOccupiedSeats += lookVertical(range(rowNum - 1, -1, -1), seatNum)

        # LOOK NW
        if seatNum > 0:
            numOccupiedSeats += lookDiagonal(range(rowNum - 1, -1, -1), seatNum, -1)

        # LOOK NE
        if seatNum < rowRight:
            numOccupiedSeats += lookDiagonal(range(rowNum - 1, -1, -1), seatNum, 1)

    # DOWN
    if rowNum < seatplanDown:
        # LOOK SOUTH
        numOccupiedSeats += lookVertical(range(rowNum + 1, seatplanDown, 1), seatNum)

        # LOOK SW
        if seatNum > 0:
            numOccupiedSeats += lookDiagonal(range(rowNum + 1, seatplanDown, 1), seatNum, -1)

        # LOOK SE    
        if seatNum < rowRight:
            numOccupiedSeats += lookDiagonal(range(rowNum + 1, seatplanDown, 1), seatNum, 1)
    
    return numOccupiedSeats

def fillSeats(mySeatplan):
    newSeatplan = [''] * len(mySeatplan)
    rowNum = 0
    for rowString in mySeatplan:
        row = list(rowString)
        seatNum = 0
        for seat in row:
            if '.' != seat:
                occupied = howManyOccupied(rowNum, seatNum)
                if 'L' == seat and occupied == 0:
                    row[seatNum] = '#'
                elif '#' == seat and occupied >= 5:
                    row[seatNum] = 'L'
            newRow = "".join(row)
            newSeatplan[rowNum] = newRow
            seatNum += 1
        rowNum += 1
    
    return newSeatplan

prevSeatplan = [''] * len(seatplan)
while prevSeatplan != seatplan:
    prevSeatplan = seatplan
    seatplan = fillSeats(seatplan)

print('Occupied seats', "".join(seatplan).count('#'))
