#!/usr/bin/python

"""Problem 30: Digit fifth powers"""

def main():
    s = 0

    powers = { str(x) : x**5 for x in range(10) }

    for n in range(2, 6*(9**5)+1):
        if n == sum(powers[i] for i in str(n)):
            s += n
    return s

if __name__ == "__main__":
    print(main())
