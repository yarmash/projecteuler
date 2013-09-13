#!/usr/bin/python2

"""Counting fractions in a range"""

# http://en.wikipedia.org/wiki/Farey_sequence
def main():
    class Fraction():
        def __init__(self, n, d):
            self.n = n
            self.d = d

        def __lt__(self, other):
            return self.n*other.d < self.d*other.n

        def __ne__(self, other):
            return self.n != other.n or self.d != other.d

    def farey_terms(n):
        high = Fraction(1, 2)

        # The next 2 terms after 1/3 are 4000/11999, 3999/11996
        a, b, c, d = 4000, 11999, 3999, 11996
        term = Fraction(a, b)

        while term != high:
            yield term
            k = (n + b)/d
            a, b, c, d = c, d, k*c - a, k*d - b
            term = Fraction(a, b)

    n = 12000
    return sum(1 for t in farey_terms(n))


if __name__ == "__main__":
    print main()
