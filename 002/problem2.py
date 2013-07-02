#!/usr/bin/python2

"""Problem 2: Even Fibonacci numbers"""

def main():
    x, y = 1, 2
    limit = 4000000
    s = 0

    while y <= limit:
        if not y&1: # even
            s += y

        x, y = y, x + y

    return s


if __name__ == "__main__":
    print main()
