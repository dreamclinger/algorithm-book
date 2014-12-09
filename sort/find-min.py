#!/usr/local/bin/env python

from random import sample, randint, random

class prettyfloat(float): ## format float number print
    def __repr__(self):
        return "%0.2f" % self

def minimum(A):
    min_element = A[0] 
    for i in range(1,len(A)):
        if min_element > A[i]:
            min_element = A[i]
    return min_element

if __name__ == '__main__':
    Array = []
    for i in range(0,10):
        Array.append(random())   ## normal random var in [0,1)
    print 'generated: ', map(prettyfloat, Array)
    L = minimum(Array)
    print 'minimum:   ', '%0.2f' % L
