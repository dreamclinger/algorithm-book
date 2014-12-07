#!/usr/local/bin/env python
# Author: dreamclinger@gmail.com
# Create: 2014/12/06
# Counting sort assumes that each of the n input elements is an integer in the range 0 to k, for some integer k.
# Counting sort determines, for each input element x, the number of elements less than x.

from random import sample, randint

def countsort(A,B,k):       ## page 195
    C = [0]*(k+1)      ## init new array C[0...k], k is num range len in A 
    for i in range(0,k+1):
        C[i] = 0
    for j in range(0,len(A)):  ## loop A[0] to A[len-1]
        C[A[j]] = C[A[j]] + 1 ## C contains the num that eq i
    for i in range(1,k): 
        C[i] = C[i] + C[i-1]  ## C contains the num that less or eq i 
    for j in range(len(A)-1,-1,-1):   ## loop A[len-1] downto A[0]
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1

if __name__ == '__main__':
    k = 5
    L = []
    Array = [0]*10
    for i in range(0,10):
        L.append(randint(1,k))
    print 'before sort: ',L
    countsort(L,Array,k)
    print 'after sort:  ',Array
