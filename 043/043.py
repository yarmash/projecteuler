#!/usr/bin/python2

from itertools import permutations

s = 0

for p in permutations((9,8,7,6,5,4,3,2,1,0)):
    if p[0] == 0:
        break

    if (p[7]*100+p[8]*10+p[9]) % 17 == 0 and \
       (p[6]*100+p[7]*10+p[8]) % 13 == 0 and \
       (p[5]*100+p[6]*10+p[7]) % 11 == 0 and \
       (p[4]*100+p[5]*10+p[6]) % 7 == 0 and \
       (p[5] == 0 or p[5] == 5) and \
       (p[2]+p[3]+p[4]) % 3 == 0 and \
       (not p[3] & 1):
        s += int("".join(map(str, p)))
print s

