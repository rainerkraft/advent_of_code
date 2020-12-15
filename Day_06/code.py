#!/usr/bin/env python3

import re
from collections import Counter

with open('input.txt', 'r') as fp:
    rawData = fp.read().rstrip()

allAnswers = list(map(lambda x: x.replace('\n', '|'), re.split(r'\n{2,}', rawData)))

part1Count = 0
part2Count = 0
for answers in allAnswers:
    uniqueAnswers = list(set(answers.replace('|', '')))
    allAnswers = list(answers)
    part1AnswersList = ''.join(sorted(uniqueAnswers))
    part1Count += len(part1AnswersList)

    part2AnswersList = answers.split('|')
    counts = Counter(part2AnswersList[0])
    for parts in part2AnswersList:
        counts &= Counter(parts)

    part2Count += len(list(counts))

print('Part 1 count: %d' % (part1Count))
print('Part 2 count: %d' % (part2Count))
