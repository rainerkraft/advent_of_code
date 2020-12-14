#!/usr/bin/env python3

with open('input.csv', 'r') as fp:
    tickets = [line.rstrip() for line in fp]

seatIds = []
for ticket in tickets:
    row = int(ticket[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(ticket[-3:].replace('R', '1').replace('L', '0'), 2)
    seatIds.append(row * 8 + col)

print(max(seatIds))
