#!/usr/bin/python

import os
import sys
import time
from heapq import nlargest

bindir = os.path.dirname(__file__)
dirs = sorted(d for d in os.listdir(bindir) if d.isdigit())
total_time = 0
results = {}

for d in dirs:
    sys.path.append(os.path.join(bindir, d))
    mod = __import__("problem"+str(int(d)))
    del sys.path[-1]
    print(d, " ", end="", flush=True)
    begin = time.clock()
    answer = str(mod.main())
    t = time.clock() - begin

    if answer == open(os.path.join(bindir, d, "answer")).read().rstrip():
        print("OK ({0:.4f}s)".format(t))
        total_time += t
        results[d] = t
    else:
        print("FAIL")
        break
else:
    print("Total: {0} problems in {1:.3f}s".format(len(dirs), total_time))
    print("\nSlowest solutions:")

    for problem in nlargest(5, results, results.get):
        print("{}  {:.2f}s".format(problem, results[problem]))
