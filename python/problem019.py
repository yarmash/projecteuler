#!/usr/bin/python

"""Problem 19: Counting Sundays"""


def is_leap_year(year):
    """Determine whether a year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
    numdays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    year, month, wday = 1901, 0, 2  # 1 Jan 1901
    sundays = 0

    while year < 2001:
        if wday == 0:
            sundays += 1

        days = 29 if month == 1 and is_leap_year(year) else numdays[month]
        wday = (wday + days) % 7

        if month < 11:
            month += 1
        else:
            month = 0
            year += 1

    return sundays

if __name__ == "__main__":
    print(main())
