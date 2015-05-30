#!/usr/bin/python

import os
import sys
from time import clock
from importlib import import_module
from heapq import nlargest


def read_answers():
    """Read the answers file"""
    with open(os.path.join(os.path.dirname(__file__), "answers")) as afile:
        answers = [line.rstrip() for line in afile]
    return answers


def run(func):
    """Time function execution"""
    begin = clock()
    answer = func()
    time = clock() - begin
    return time, answer


def main():
    answers = read_answers()

    if len(sys.argv) == 2:
        problems = [int(sys.argv[1])]
    else:
        problems = list(range(1, len(answers)+1))

    total_time = 0
    results = {}

    for num in problems:
        mod_name = "problem{:03d}".format(num)
        mod = import_module(mod_name)

        print("{:03d}".format(num), " ", end="", flush=True)
        time, answer = run(mod.main)
        if str(answer) != answers[num-1]:
            print("FAIL ({} != {})".format(answer, answers[num-1]))
            return

        print("OK ({0:.6f}s)".format(time))
        total_time += time
        results[num] = time

    if len(problems) > 1:
        print("Total: {} problems in {:.3f}s".format(len(problems),
                                                     total_time))
        print("\nSlowest solutions:")

        for problem in nlargest(5, results, results.get):
            print("{:03d}  {:.2f}s".format(problem, results[problem]))

if __name__ == '__main__':
    main()
