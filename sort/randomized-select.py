#!/usr/local/bin/env python
# Author: dreamclinger@gmail.com
# Create: 2014/12/09
# The following code for randomize-select returns the ith smallest element of the array A[p...r]. page 216

from random import sample 
from random import randint 


def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i] ## exchange A[i] and A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def randomized_partition(A,p,r):  ## in quick-sort.py
    i = randint(p,r)         
    A[r], A[i] = A[i], A[r]
    return partition(A,p,r)

def randomized_select(A,p,r,i):
    if p == r:
        return A[p]
    q = randomized_partition(A,p,r)
    k = q-p+1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A,p,q-1,i)
    else:
        return randomized_select(A,q+1,r,i-k)

if __name__ == '__main__':
    maxnum = 10
    i = randint(1,maxnum)
    Array = sample(range(1,20),maxnum)
    print 'generated: ',Array
    key = randomized_select(Array,0,len(Array)-1,i)
    print 'the',i,'th smallest number: ',key
