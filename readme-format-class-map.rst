class map, for format printing
====

from random import sample, randint, random
from math import floor
import formatter

class prettyfloat(float): ## format float number print
    def __repr__(self):
        return "%0.2f" % self

if __name__ == '__main__':
    Array = []
    for i in range(0,10):
        Array.append(random())   ## normal random var in [0,1)
    print 'before sort: ', map(prettyfloat, Array)
