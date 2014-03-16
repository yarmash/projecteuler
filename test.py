#!/usr/bin/python

import os
import sys
import time

bindir = os.path.dirname(__file__)
dirs = sorted(d for d in os.listdir(bindir) if d.isdigit())
total_time = 0
runs = {}

for d in dirs:
    sys.path.append(os.path.join(bindir, d))
    mod = __import__("problem"+str(int(d)))
    sys.path.pop()
    answer = open(os.path.join(bindir, d, "answer")).read().rstrip()
    sys.stdout.write(d+"  ")
    sys.stdout.flush()
    begin = time.clock()

    if answer == str(mod.main()):
        t = time.clock() - begin
        total_time += t
        runs[d] = t
        print("OK ({0:.2f}s)".format(t))
    else:
        print("FAIL")

print("Total: {0} problems in {1:.2f}s".format(len(dirs), total_time))

slowpokes = sorted(((v, k) for k, v in runs.items()), reverse=True)[0:5]

print("\nSlowest solutions:")

for s in slowpokes:
    print("{1}  {0:.2f}s".format(*s))
