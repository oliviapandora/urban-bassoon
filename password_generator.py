import random

LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL_CHAR = '~!@#$%^&*()_+'
TOTAL = LOWERCASE + UPPERCASE + NUMBERS + SPECIAL_CHAR

def generatePassword(length):
    if length < 12:
        length = 12
    password = []
    password.append(LOWERCASE[random.randint(0, 25)])
    password.append(UPPERCASE[random.randint(0, 25)])
    password.append(NUMBERS[random.randint(0, 9)])
    password.append(SPECIAL_CHAR[random.randint(0, 12)])

    while len(password) < length:
        password.append(TOTAL[random.randint(0, 74)])

    random.shuffle(password)
    
    return''.join(password)

assert len(generatePassword(8)) == 12


pw = generatePassword(14)
assert len(pw) == 14
hasLOWERCASE = False
hasUPPERCASE = False
hasNUMBERS = False
hasSPECIAL_CHAR = False
for character in pw:
    if character in LOWERCASE:
        hasLOWERCASE = True
    if character in UPPERCASE:
        hasUPPERCASE = True
    if character in NUMBERS:
        hasNUMBERS = True
    if character in SPECIAL_CHAR:
        hasSPECIAL_CHAR = True
assert hasLOWERCASE and hasUPPERCASE and hasNUMBERS and hasSPECIAL_CHAR