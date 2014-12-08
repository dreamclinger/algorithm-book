#!/usr/local/bin/env python
# Author: dreamclinger@gmail.com
# Create: 2014/12/06

from random import sample 
from random import randint 
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

def randomized_partition(A,p,r):  ## page 179
    i = randint(p,r)         ##rand num in [p,r] ;while sample returns list
    A[r], A[i] = A[i], A[r]
    return partition(A,p,r)

def randomized_quicksort(A,p,r):
    if p < r:
        q = randomized_partition(A,p,r)
        randomized_quicksort(A,p,q-1)
        randomized_quicksort(A,q+1,r)

if __name__ == '__main__':
    maxnum = 10
    Array1 = sample(range(1,20),maxnum)
    Array2 = Array1
    print 'before sort: ',Array1
    quicksort(Array1,0,len(Array1)-1)
    print 'after sort:  ',Array1
    randomized_quicksort(Array2,0,len(Array2)-1)
    print 'randomized:  ',Array2
