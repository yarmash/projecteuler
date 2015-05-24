#!/usr/bin/python

"""Problem 101: Optimum polynomial"""

from sympy import symbols, solve


def main():

    # create some symbols for our equations
    variables = symbols("a b c d e f g h i j k")

    terms = [
        1 - x + x**2 - x**3 + x**4 - x**5 + x**6 - x**7 + x**8 - x**9 + x**10
        for x in range(1, 12)]

    fits_sum = 1

    for n in range(2, 11):
        system = []

        for x in range(1, n+1):
            eq = sum([var*x**exp for var, exp in
                      zip(variables, range(n-1, -1, -1))]) - terms[x-1]
            system.append(eq)

        solution = solve(system, variables[:n])

        fits_sum += sum([solution[var]*(n+1)**exp for var, exp in
                         zip(variables, range(n-1, -1, -1))])
    return fits_sum

if __name__ == "__main__":
    print(main())
