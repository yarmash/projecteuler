#!/usr/bin/env python2

import os
import sys
import time

bindir = os.path.dirname(__file__)

dirs = sorted([ d for d in os.listdir(bindir) if d.isdigit() ])

start = time.clock()
cnt = 0
for d in dirs:
    cnt += 1
    sys.path.insert(0, os.path.join(bindir, d))
    mod =  __import__("problem"+str(int(d)))
    sys.path.pop(0)
    answer = open(os.path.join(bindir, d, "answer")).read().rstrip()
    sys.stdout.write(d+"  ")
    sys.stdout.flush()
    begin = time.clock()
    if answer == str(mod.main()):
        print "OK (%.2fs)" % (time.clock() - begin)
    else:
        print "FAIL"

print "Total: %d problems in %.2fs" % (cnt, time.clock()-start)
