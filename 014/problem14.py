#!/usr/bin/python2

"""Problem 14: Longest Collatz sequence"""

def main():
    cache = {}
    longest = 0
    num = 0

    def get_chain_length(n):
        if n == 2:
            return 2

        if not n in cache:
            cache[n] = 2 + get_chain_length((3*n+1) >> 1) if n&1 else 1 + get_chain_length(n>>1)
        return cache[n]

    for i in xrange(2, 1000000):
        length = get_chain_length(i)

        if length > longest:
            longest = length
            num = i

    return num

if __name__ == "__main__":
    print main()
