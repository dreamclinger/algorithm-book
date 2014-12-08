#!/usr/local/bin/env python
# Author: dreamclinger@gmail.com
# Create: 2014/12/03

from random import sample

def insertsort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

if __name__ == '__main__':
    Array = sample(range(1,20),10)
    print 'before sort: ',Array
    insertsort(Array)
    print 'after sort:  ',Array
