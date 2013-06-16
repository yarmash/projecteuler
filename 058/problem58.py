#!/usr/bin/python2

from miller_rabin import miller_rabin as is_prime

def main():
    number = 1
    cnt = 0
    step = 2
    primes_cnt = 0

    while True:
        cnt += 1
        number += step

        if cnt & 3: # only the first 3 diagonals contain primes
            primes_cnt += is_prime(number)
        else:
            # layer done
            if primes_cnt/(2*step+1.0) < .1: # ratio below 10%
                return 1+step
            step += 2

    return result

if __name__ == "__main__":
    print main()
