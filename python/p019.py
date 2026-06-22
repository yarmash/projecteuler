#!/usr/bin/env python3

"""Problem 19: Counting Sundays"""

from calendar import isleap as is_leap_year


def main():
    numdays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    weekday = 2  # Tuesday, 1 Jan 1901, with Sunday represented as 0
    sundays = 0

    for year in range(1901, 2001):
        is_leap = is_leap_year(year)
        for month in range(12):
            if weekday == 0:
                sundays += 1
            days = 29 if is_leap and month == 1 else numdays[month]
            weekday = (weekday + days) % 7

    return sundays


if __name__ == "__main__":
    print(main())
