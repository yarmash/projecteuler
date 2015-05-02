#!/usr/bin/python

"""Problem 42: Coded triangle numbers"""

from utils import open_data_file, is_triangular_number


def main():
    with open_data_file("words.txt") as data_file:
        words = [word[1:-1] for word in data_file.read().split(",")]

    return sum([is_triangular_number(sum([ord(char)-64 for char in word]))
                for word in words])

if __name__ == "__main__":
    print(main())
