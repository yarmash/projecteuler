#!/usr/bin/python

import os
import time
import itertools
from importlib import import_module
from heapq import nlargest


def main():
    total_time = 0
    results = {}

    with open(os.path.join(os.path.dirname(__file__), "answers")) as f:
        answers = [line.rstrip() for line in f]

    for i in itertools.count(1):
        mod_name = "problem{:03d}".format(i)
        try:
            mod = import_module(mod_name)
        except ImportError as exc:
            if exc.name != mod_name:
                raise
            i -= 1
            break
        print("{:03d}".format(i), " ", end="", flush=True)
        begin = time.clock()
        answer = str(mod.main())
        t = time.clock() - begin

        if answer == answers[i-1]:
            print("OK ({0:.6f}s)".format(t))
            total_time += t
            results[i] = t
        else:
            print("FAIL")
            return
    print("Total: {} problems in {:.3f}s".format(i, total_time))
    print("\nSlowest solutions:")

    for problem in nlargest(5, results, results.get):
        print("{:03d}  {:.2f}s".format(problem, results[problem]))

if __name__ == '__main__':
    main()
