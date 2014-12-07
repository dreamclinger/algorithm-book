#!/usr/local/bin/env python
# Author: dreamclinger@gmail.com
# Create: 2014/12/06

from random import sample 
from math import floor


def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i] ## exchange A[i] and A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

if __name__ == '__main__':
    maxnum = 10
    Array = sample(range(1,20),maxnum)
    print 'before sort: ',Array
    quicksort(Array,0,len(Array)-1)
    print 'after sort:  ',Array
