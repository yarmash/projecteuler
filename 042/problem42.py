#!/usr/bin/python

"""Problem 42: Coded triangle numbers"""

from projecteuler import data_file, is_triangular_number


def main():
    with open(data_file("words.txt")) as f:
        words = eval("["+f.read()+"]")

    cnt = 0

    for word in words:
        if is_triangular_number(sum([ord(c)-64 for c in word])):
            cnt += 1

    return cnt

if __name__ == "__main__":
    print(main())
