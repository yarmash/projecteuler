#!/usr/bin/python2

def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    return False

numdays = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

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

print cnt
