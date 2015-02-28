#!/usr/bin/python

"""Problem 42: Coded triangle numbers"""

from projecteuler import data_file, is_triangular_number


def main():
    with open(data_file("words.txt")) as f:
        words = eval("["+f.read()+"]")

    return sum([is_triangular_number(sum([ord(char)-64 for char in word]))
                for word in words])

if __name__ == "__main__":
    print(main())
