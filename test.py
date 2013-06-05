#!/usr/bin/env python2

import os
import re
import sys
import time

bindir = os.path.dirname(__file__)

dirs = sorted([ d for d in os.listdir(bindir) if re.match('[0-9]{3}$', d) ])

for d in dirs:
    sys.path.insert(0, os.path.join(bindir, d))
    mod =  __import__("problem"+str(int(d)))
    answer = open(os.path.join(bindir, d, "answer")).read().rstrip()
    print d+" ",
    start = time.clock()
    if answer == str(mod.main()):
        print "OK (%.2fs)" % (time.clock() - start)
    else:
        print "FAIL"
    sys.path.pop(0)
