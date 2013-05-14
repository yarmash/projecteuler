#!/usr/bin/python2

res = 0

for c1 in [1*x for x in range(201)]:
    s = c1
    if s >= 200:
        if s == 200: res += 1
        break

    for c2 in [2*x for x in range(101)]:
        s = c1+c2
        if s >= 200:
            if s == 200: res += 1
            break

        for c5 in [5*x for x in range(41)]:
            s = c1+c2+c5
            if s >= 200:
                if s == 200: res += 1
                break

            for c10 in [10*x for x in range(21)]:
                s = c1+c2+c5+c10
                if s >= 200:
                    if s == 200: res += 1
                    break

                for c20 in [20*x for x in range(11)]:
                    s = c1+c2+c5+c10+c20
                    if s >= 200:
                        if s == 200: res += 1
                        break

                    for c50 in [50*x for x in range(5)]:
                        s = c1+c2+c5+c10+c20+c50
                        if s >= 200:
                            if s == 200: res += 1
                            break

                        for c100 in [100*x for x in range(3)]:
                            s = c1+c2+c5+c10+c20+c50+c100
                            if s >= 200:
                                if s == 200: res += 1
                                break

                            for c200 in [200*x for x in range(2)]:
                                s = c1+c2+c5+c10+c20+c50+c100+c200
                                if s >= 200:
                                    if s == 200: res += 1
                                    break


print res
