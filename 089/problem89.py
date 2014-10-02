#!/usr/bin/python

"""Problem 89: Roman numerals"""

from projecteuler import open_data_file


def main():
    chars_saved = 0

    # From the problem definition:
    # You can assume that all the Roman numerals in the file contain no more
    # than four consecutive identical units.

    for line in open_data_file("roman.txt"):
        if "VIIII" in line:
            chars_saved += 3  # VIIII => IX
        elif "IIII" in line:
            chars_saved += 2  # IIII => IV

        if "LXXXX" in line:
            chars_saved += 3  # LXXXX => XC
        elif "XXXX" in line:
            chars_saved += 2  # XXXX => XL

        if "DCCCC" in line:
            chars_saved += 3  # DCCCC => CM
        elif "CCCC" in line:
            chars_saved += 2  # CCCC => CD

    return chars_saved


if __name__ == "__main__":
    print(main())
