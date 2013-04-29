#!/usr/bin/python2

print sum([ int(i) for i in str( reduce(lambda x,y: x*y, range(1, 100)) ) ])
