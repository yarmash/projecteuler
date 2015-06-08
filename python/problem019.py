#!/usr/bin/python

"""Problem 19: Counting Sundays"""


def is_leap_year(year):
    """Determine whether a year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
    numdays = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    year, month, wday = 1901, 1, 2
    cnt = 0

    while year < 2001:
        if wday == 0:
            cnt += 1

        days = 29 if month == 2 and is_leap_year(year) else numdays[month-1]
        wday = (wday + days) % 7

        month += 1

        if month > 12:
            year += 1
            month = 1

    return cnt

if __name__ == "__main__":
    print(main())
