#!/usr/bin/python

"""Verify and benchmark solutions"""

import os
import sys
from time import clock
from importlib import import_module
from heapq import nlargest
from concurrent.futures import ProcessPoolExecutor


def read_answers():
    """Read the answers file"""
    filename = os.path.join(os.path.dirname(__file__), "answers")
    with open(filename) as f:
        return [line.rstrip() for line in f]


def run(num):
    """Run the solution and measure the execution time"""
    mod_name = f"problem{num:03d}"
    mod = import_module(mod_name)

    begin = clock()
    answer = mod.main()
    time = clock() - begin

    return answer, time


def main():
    answers = read_answers()

    if len(sys.argv) == 2:
        problems = [int(sys.argv[1])]
    else:
        problems = list(range(1, len(answers)+1))

    total_time = 0
    times = {}

    with ProcessPoolExecutor() as executor:
        for num, (answer, time) in zip(problems, executor.map(run, problems,
                                                              chunksize=2)):
            print(f"{num:03d} ", end="")

            if str(answer) != answers[num-1]:
                print(f"FAIL ({answer} != {answers[num-1]})")
                return 1

            print(f"OK ({time:.6f}s)")
            total_time += time
            times[num] = time

    if len(problems) > 1:
        print(f"\nTotal {len(problems)} problems solved.\n")
        print("Slowest solutions:")

        for problem in nlargest(5, times, times.get):
            print(f"{problem:03d}  {times[problem]:.2f}s {times[problem]/total_time:6.2%}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
