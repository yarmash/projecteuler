#!/usr/bin/python2

"""Totient permutation"""

from projecteuler import prime_sieve, is_permutation
from Queue import PriorityQueue

def main():
    # n cannot be prime^k (k = [1, 2, ...]) because prime^k and phi(prime^k)
    # cannot be a permutation of each other

    lim = 10**7
    primes = prime_sieve(5000)

    def gen_product(start):
        i = len(primes) - 1

        while primes[start]*primes[i] > lim:
            i -= 1

        for j in xrange(i, start, -1):
            yield (primes[start], primes[j])


    def n_by_phi(p1, p2):
        return float(p1*p2)/((p1-1)*(p2-1))


    def sorted_by_ratio():
        queue = PriorityQueue()

        # the max prime <= sqrt(10**7) is 3137, which has the index of 445
        middle_idx, middle = 445, 3137

        for i in xrange(middle_idx, -1, -1):
            it = gen_product(i)
            pair = it.next()
            queue.put((n_by_phi(*pair), pair, it))


        while not queue.empty():
            factor, pair, it = queue.get()
            yield pair

            try:
                pair = it.next()
                queue.put((n_by_phi(*pair), pair, it))
            except StopIteration:
                pass

    for p1, p2 in sorted_by_ratio():
        if is_permutation(p1*p2, (p1-1)*(p2-1)):
            return p1*p2


if __name__ == "__main__":
    print main()
