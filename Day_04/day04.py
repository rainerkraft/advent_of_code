#!/usr/bin/env python3

import re

def isIdDocValid(idDoc):
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    missingFields = list(set(requiredFields) - set(idDoc.keys()))
    numMissingFields = len(missingFields)
    if numMissingFields == 0:
        return True
    elif numMissingFields == 1:
        return True if missingFields.count('cid') == 1 else False
    return False

idDocuments = []
with open('input.csv', 'r') as fp:
    rawData = fp.read().rstrip()

idDocuments = list(map(lambda x: x.replace('\n', ' '), re.split(r'\n{2,}', rawData)))
idDocuments = [ re.split(r' ', idDoc) for idDoc in idDocuments ]

validDocs = 0;
for idDoc in idDocuments:
    idDoc = dict(fieldPair.split(':', 1) for fieldPair in idDoc)
    validDocs += 1 if isIdDocValid(idDoc) else 0

print('Valid docs (no fields missing): %d' % validDocs)
