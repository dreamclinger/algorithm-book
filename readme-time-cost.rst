pseudo-code in book
====
for j = 2 to A.length  ## c1*n 
    key = A[j]         ## c2*(n-1)
    //Insert A[j] in to the sorted sequence A[1,2,...j-1].
    i = j - 1          ## c4*n-1
    while i > 0 and A[i] > key  ## c5*($\sum_{j=2}^{n} t_j$
        A[i+1] = A[i]           ## c6*($\sum_{j=2}^{n} (t_j - 1)$
        i = i - 1               ## c7*($\sum_{j=2}^{n} (t_j - 1)$
    A[i+1] = key                ## c8*(n-1)

> c1, c2, ... c8 is the individual cost for each single step;
> n = A.length
> assume: t_j = 1; c1 = c2 = ... = c8 = constant (actually it's linear)
> add them together you find O(n^2)

real-code in python, notice the index begins from 0, not 1
====
for j in range(1,len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
