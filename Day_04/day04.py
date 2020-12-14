#!/usr/bin/env python3

import re

# Field Validation
# ---------------------------------------------------------------------
# - byr (Birth Year) - four digits; at least 1920 and at most 2002.
# - iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# - hgt (Height) - a number followed by either cm or in:
#   - If cm, the number must be at least 150 and at most 193.
#   - If in, the number must be at least 59 and at most 76.
# - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# - pid (Passport ID) - a nine-digit number, including leading zeroes.
# - cid (Country ID) - ignored, missing or not.
# ---------------------------------------------------------------------

def isValid(idDoc):
    if False == hasAllRequiredFields(idDoc):
        return False

    # - byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if False == (None != re.search('^\d{4}$', idDoc['byr']) and 1920 <= int(idDoc['byr']) <= 2002):
        return False

    # - iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    if False == (None != re.search('^\d{4}$', idDoc['iyr']) and 2010 <= int(idDoc['iyr']) <= 2020):
        return False

    # - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    if False == (None != re.search('^\d{4}$', idDoc['eyr']) and 2020 <= int(idDoc['eyr']) <= 2030):
        return False

    # - hgt (Height) - a number followed by either cm or in:
    #   - If cm, the number must be at least 150 and at most 193.
    #   - If in, the number must be at least 59 and at most 76.
    if None == re.search('^\d{2,3}(cm|in)$', idDoc['hgt']):
        return False

    match = re.search(r'\d+', idDoc['hgt'])
    if False == (
        (None != re.search('^\d+cm$', idDoc['hgt']) and 150 <= int(match.group()) <= 193)
        or
        (None != re.search('^\d+in$', idDoc['hgt']) and 59 <= int(match.group()) <= 76)
    ):
        return False

    # - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    if None == re.search('^\#[0-9a-f]{6}$', idDoc['hcl']):
        return False

    # - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if None == re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', idDoc['ecl']):
        return False

    # - pid (Passport ID) - a nine-digit number, including leading zeroes.
    if None == re.search('^[0-9]{9}$', idDoc['pid']):
        return False

    return True

def hasAllRequiredFields(idDoc):
    requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    missingFields = list(set(requiredFields) - set(idDoc.keys()))
    numMissingFields = len(missingFields)
    if numMissingFields == 0:
        return True
    elif numMissingFields == 1:
        return True if missingFields.count('cid') == 1 else False
    return False

with open('input.csv', 'r') as fp:
    rawData = fp.read().rstrip()

idDocuments = list(map(lambda x: x.replace('\n', ' '), re.split(r'\n{2,}', rawData)))
idDocuments = [ re.split(r' ', idDoc) for idDoc in idDocuments ]

validDocs = 0;
for idDoc in idDocuments:
    idDoc = dict(fieldPair.split(':', 1) for fieldPair in idDoc)
    validDocs += 1 if isValid(idDoc) else 0

print('Valid docs (no fields missing): %d' % validDocs)
