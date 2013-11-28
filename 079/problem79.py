#!/usr/bin/python

"""Problem 79: Passcode derivation"""

import re
from itertools import permutations
from projecteuler import open_data_file

def main():
    passcodes = open_data_file("keylog.txt").read().splitlines()

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
