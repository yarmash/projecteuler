#!/usr/bin/python2

import itertools

cnt = 0
for p in itertools.permutations(range(10)):
    cnt += 1
    if cnt == 1000000:
        print "".join(map(str, p))
        break
