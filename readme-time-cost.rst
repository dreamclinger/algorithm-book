pseudo-code in book, e.g. insert-sort.py
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

divide-and-conquer analysis, e.g. merge-sort.py
====
T(n) = aT(n/b) + D(n) + C(n), when n > constant; otherwise T(n) = O(1)

> each division yields a subproblems,
> where each subproblem is 1/b size of the original.
> time for dividing is D(n)
> time for combining the solution is C(n)

