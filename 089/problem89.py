#!/usr/bin/python

"""Problem 89: Roman numerals"""

from projecteuler import open_data_file

VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,

    # subtractive combinations
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}

NUMERALS = sorted(VALUES, key=VALUES.get, reverse=True)


def roman_to_arabic(roman):
    """Convert a roman numeral to arabic number"""
    arabic = 0

    for i in range(len(roman)-1):
        if VALUES[roman[i]] < VALUES[roman[i+1]]:
            arabic -= VALUES[roman[i]]
        else:
            arabic += VALUES[roman[i]]
    arabic += VALUES[roman[-1]]

    return arabic


def arabic_to_roman(arabic):
    """Convert an arabic number to roman numeral in the minimal form"""
    numerals = []

    for numeral in NUMERALS:
        while arabic >= VALUES[numeral]:
            arabic -= VALUES[numeral]
            numerals.append(numeral)
    return "".join(numerals)


def main():
    saved_chars = 0

    for line in open_data_file("roman.txt"):
        line = line.rstrip()
        saved_chars += len(line) - len(arabic_to_roman(roman_to_arabic(line)))

    return saved_chars


if __name__ == "__main__":
    print(main())
