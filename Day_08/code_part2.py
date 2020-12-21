#!/usr/bin/env python3

with open('input.txt', 'r') as fp:
    lines = [line.rstrip() for line in fp]

numLines = len(lines)
counts = [0] * numLines
accumulator = 0
prevIndex = 0
index = 0

# Very ugly but it works...

def chickenRun(sub, whichSubCount):
    counter = 0
    subCounter = 0
    hasSubstituted = False
    global index
    global accumulator
    global numLines
    global counts

    try:
        while True:
            [instruction, value] = lines[index].split(' ')

            if instruction == 'acc':
                accumulator += int(value)
                index += 1
            elif instruction == 'jmp':
                if whichSubCount == subCounter and hasSubstituted == False and sub == 'jmp':
                    hasSubstituted = True
                    index += 1
                else:
                    index += int(value)
            else:
                if whichSubCount == subCounter and hasSubstituted == False and sub == 'nop':
                    hasSubstituted = True
                    index += int(value)
                else:
                    index += 1

            counts[index] += 1

            if sub == instruction:
                subCounter += 1

            if counts[index] > 1:
                return False

            counter += 1

    except IndexError:
        return True

    return True

for sub in ['nop', 'jmp']:
    for i in range(0, numLines - 1):
        accumulator = 0
        counts = [0] * numLines
        index = 0
        result = chickenRun(sub, i)
        if result == True:
            break
    else:
        continue
    break


print('RESULT: %s, ACC: %d' % (result, accumulator))
