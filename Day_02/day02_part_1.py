#!/usr/bin/env python3

# import itertools
import re

with open('input.csv') as fp:
    foo = [re.split(' |: |-', line.rstrip()) for line in fp]

countValidPasswordsPart1 = 0;
countValidPasswordsPart2 = 0;
for rule in foo:
    min = int(rule[0])
    max = int(rule[1])
    letter = str(rule[2])
    password = str(rule[3])
    countLetter = password.count(letter)
    countValidPasswordsPart1 += 1 if countLetter >= min and countLetter <= max else 0
    atLeastOnce = True if password[min-1] == letter or password[max-1] == letter else False
    notTwice = False if password[min-1] == letter and password[max-1] == letter else True
    countValidPasswordsPart2 += 1 if atLeastOnce and notTwice else 0
    print(min, max, letter, password, password[min-1], password[max-1], countValidPasswordsPart2)

print('Valid passwords Part 1: ', countValidPasswordsPart1)
print('Valid passwords Part 2: ', countValidPasswordsPart2)
