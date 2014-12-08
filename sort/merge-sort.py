#!/usr/local/bin/env python
# Author: dreamclinger@gmail.com
# Create: 2014/12/03

from random import sample 
from math import floor


def merge(A,p,q,r):
    n1 = q-p+1          ## [p ... q]
    n2 = r-q            ## [q+1 ... r]
    L = []
    R = []
    for i in range(0,n1):
            L.append(A[p+i])
    for j in range(0,n2):
            R.append(A[q+j+1]) 
            #R[j] = A[q+j+1]   ## error in list index out of range 
    L.append(float("inf"))  ## inf+ number for easy-compare and stop search
    R.append(float("inf"))
    i = 0
    j = 0
    for k in range(p,r+1):    ## merge L and R to A
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else: 
            A[k] = R[j]
            j = j + 1
    return A

def mergesort(A,p,r):
    if p < r:
        q = int(floor((p+r)/2))
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)

if __name__ == '__main__':
    maxnum = 10
    Array = sample(range(1,20),maxnum)
    print 'before sort: ',Array
    mergesort(Array,0,len(Array)-1)   ## python assumes you revise the passing array, then no return
    print 'after sort:  ',Array
