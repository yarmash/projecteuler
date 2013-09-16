#!/usr/bin/python2

"""Problem 51: Prime digit replacements"""

from euler import is_prime


def main():
    num = 1009 # 1st 4-digit prime

    while True:
        num += 2

        if is_prime(num):
            s = str(num)

            for c in "012":
                count = s.count(c)

                # count has to be a multiple of 3
                if count and count % 3 == 0 and not (c == "1" and s[-1] == "1"):
                    cnt = 1

                    for i in xrange(int(c)+1, 10):
                        if 10-i < 8-cnt: break

                        if is_prime(int(s.replace(c, str(i)))):
                            cnt += 1
                            if cnt == 8:
                                return num
if __name__ == '__main__':
    print main()
