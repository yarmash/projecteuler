#!/usr/bin/python2

from itertools import permutations

s = 0

for p in permutations("1234567890"):
    p = "".join(p)
    if p[0] == "0":
        continue

    if int(p[1:4]) % 2 == 0 and \
       int(p[2:5]) % 3 == 0 and \
       int(p[3:6]) % 5 == 0 and \
       int(p[4:7]) % 7 == 0 and \
       int(p[5:8]) % 11 == 0 and \
       int(p[6:9]) % 13 == 0 and \
       int(p[7:10]) % 17 == 0:
        s += int(p)
print s

