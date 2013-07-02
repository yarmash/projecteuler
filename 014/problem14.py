#!/usr/bin/python2

"""Problem 14: Longest Collatz sequence"""

def main():
    cache = {}
    longest = 0
    num = 0

    def get_chain_length(n):
        if n in cache:
            return cache[n]

        if n == 1:
            cache[n] = length = 1
        else:
            cache[n] = length = 1 + get_chain_length(3*n+1 if n&1 else n>>1)
        return length

    for i in xrange(2, 1000000):
        length = get_chain_length(i)

        if length > longest:
            longest = length
            num = i

    return num

if __name__ == "__main__":
    print main()
