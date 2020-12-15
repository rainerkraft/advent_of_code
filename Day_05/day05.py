#!/usr/bin/env python3

with open('input.csv', 'r') as fp:
    tickets = [line.rstrip() for line in fp]

seatIds = []
for ticket in tickets:
    row = int(ticket[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(ticket[-3:].replace('R', '1').replace('L', '0'), 2)
    seatIds.append(row * 8 + col)

seatIds.sort()

# Part 1
print('Part 1 - Highest seat id: %d' % (seatIds[-1]))

startId = seatIds[0]
counter = 0
for seatId in seatIds:
    expectedSeatId = startId + counter
    if (
        seatId != expectedSeatId and
        (expectedSeatId in seatIds) == False and
        (expectedSeatId + 1) in seatIds and
        (expectedSeatId - 1) in seatIds
    ):
        # Part 2
        print('Part 2 - My seat id: %d' % (expectedSeatId))
        break
    counter += 1
