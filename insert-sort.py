#!/usr/local/bin/env python
# Author: dreamclinger@gmail.com
# Create: 2014/12/03

import random

def insertsort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

if __name__ == '__main__':
    Array = random.sample(range(1,20),10)
    print 'before sort: ',Array
    B = insertsort(Array)
    print 'after sort:  ',B
