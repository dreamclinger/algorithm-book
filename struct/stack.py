#!/usr/local/bin/env python
# Author: dreamclinger@gmail.com
# Create: 2014/12/09
# Now I don't use exsiting method in python (push, pop, appendix) 
# http://www.c4learn.com/c-programs/c-program-to-implement-stack-operations-using-array.html 
# The stack consists of elements S[0...S.top], where S[0] is the element at the bottom of the stack. When S.top = -1, the stack is empty

from random import sample, randint, random
from math import floor
import sys


class MyStack(object):

    def __init__(self, n=10):
        self.n = n
        self.data = [0]*n
        self.top = -1

    def stack_empty(self):
        if self.top == -1:      ## index: S[-1](empty), S[0] ... S[n-1]
            return True
        else:
            return False

    def stack_full(self):
        if self.top == self.n-1:  ## index: S[0] .... S[n-1], (full)
            return True
        else:
            return False

    def push(self,data):
        if self.stack_full() == True:
            msg = 'exception: stack full, push fails'
            sys.stderr.write('%s\n' % (msg))
        else:
            self.top = self.top + 1    ## top+1 before S->data
            self.data[self.top] = data

    def pop(self):
        if self.stack_empty() == True:
            msg = 'exception: stack empty, pop fails'
            sys.stderr.write('%s\n' % (msg))
            sys.exit(1)
        else:
            self.top = self.top - 1     ## top-1 before S->data
            return self.data[self.top+1]  

if __name__ == '__main__':
    S = MyStack(5)
    for i in range(0,6):
        num = randint(1,10)
        S.push(num)   
        print 'push',num,', stack =',S.data
    print '-' *35
    for i in range(0,6):
        print 'pop',S.pop(),', stack =',S.data 
