#!/usr/local/bin/env python
# Author: dreamclinger@gmail.com
# Create: 2014/12/03

from random import sample 
from math import floor


def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    for i in range(1,n1):
            L[i] = A[p+i-1]
    for j in range(1,n2):
            R[j] = A[q+j]
    L[n1] = 100  ## extreme-large number for easy-stop searching 
    R[n2] = 100
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else: 
            A[k] = R[j]
            j = j + 1

def mergesort(A,p,r):
    if p < r:
        q = int((p+r)/2)
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)
     #return A   

if __name__ == '__main__':
    maxnum = 10
    Array = sample(range(1,20),maxnum)
    print 'before sort: ',Array
    B = mergesort(Array,0,len(Array)-1)
    print 'after sort:  ',B
