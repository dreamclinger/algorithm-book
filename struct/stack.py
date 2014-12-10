#!/usr/local/bin/env python
# Author: dreamclinger@gmail.com
# Create: 2014/12/09


from random import sample, randint, random
from math import floor

##stack? use one first? Class?

class Stack(object):
    
    def __init__(self):
        self.storage = []
    
    def isEmpty(self):
        return len(self.storage) == 0
    
    def push(self,p):
        self.storage[:0] = p
    
    def pop(self):
        """issue: throw exception?"""
        return None


def stack_empty(S):
    if S.top == 0:
        return True
    else
        return False

def push(S,x):
    S.top = S.top + 1
    S[S.top] = x

def pop(S):
    if stack_empty(S):
        #error(underflow)
    else 
        S.top = S.top - 1
        return S[S.top+1]

if __name__ == '__main__':
    Array = []
    for i in range(0,10):
        Array.append(random())   ## normal random var in [0,1)
    print 'before sort: ', map(prettyfloat, Array)
    Newarray = bucketsort(Array)
    print 'after sort:  ', map(prettyfloat, Newarray)
