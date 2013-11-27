#!/usr/bin/python

"""Problem 79: Passcode derivation"""

import os
import re
from itertools import permutations


def main():
    datafile = os.path.join(os.path.dirname(__file__), "keylog.txt")
    passcodes = open(datafile).read().split()

    all_chars = set()
    res = []

    for passcode in passcodes:
        chars = []

        for char in passcode:
            chars.append(char)
            all_chars.add(char)

        res.append(".*".join(chars))


    for candidate in permutations(all_chars):
        passcode = "".join(candidate)

        for r in res:
            if not re.search(r, passcode):
                break
        else:
            return passcode


if __name__ == "__main__":
    print(main())
