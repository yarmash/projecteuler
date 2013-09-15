#!/usr/bin/python2

"""Digit factorial chains"""

def main():
    lim = 1000000

    factorials = [
        1,
        1,
        2,
        6,
        24,
        120,
        720,
        5040,
        40320,
        362880,
    ]

    cache = [0]*(factorials[9]*6 + 1)

    def get_chain_len(n):

        if cache[n]:
            return cache[n]

        chain = [n]

        while True:
            fsum = 0

            while n:
                fsum += factorials[n % 10]
                n /= 10

            if cache[fsum]:
                length = cache[fsum] + len(chain)

                for i, v in enumerate(chain):
                    cache[v] = length - i

                return length

            if fsum in chain:
                for i, v in enumerate(chain):
                    if v == fsum and i > 0:
                        break
                    cache[v] = len(chain) - i

                return len(chain)

            chain.append(fsum)
            n = fsum

    return sum(1 for i in xrange(lim) if get_chain_len(i) == 60)


if __name__ == "__main__":
    print main()
