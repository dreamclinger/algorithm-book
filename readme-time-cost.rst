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

recursion-tree method, for solving recurrences
====
like the above e.g. in analysis of merge-sort.py

substitution method, for solving recurrences
====
The substitution method for solving recurrences comprises two steps:
1. Guess the form of the solution. 
2. Use mathematical induction to find the constants and show that the solution works. page.83

The master method for solving recurrences, rely on O(f(n)), diff in n^e
====
Let a => 1 and b > 1 be constants, let f(n) be a function, and let T(n) be defined on the nonnegative integers by the recurrence: page.94
> T(n) = aT(n/b) + f(n)
where we interpret n/b to mean [n/c]. Then T(n) has the following asymptoticbounds: 
1. If f(n) = O(n^logb(a-e), O-upper bound, for some constant e > 0, then T(n) = O(n^logb(a)), O-equal bound.
2. If f(n) = O(n^logb(a), O-equal bound, then T(n)=O(lgn*n^logb(a)), O-equal bound.
3. If f(n) = O(n^logb(a+e), O-lower bound, for some constant e > 0, and if af(n/b) =< cf(n) for some constant c < 1 and all sufficiently large n, then T(n) = O(f(n)), O-equal bound.

> Notice case 3 isn't complete.
> the NOT contained case has an example as: T(n) = 2T(n/2) + nlgn. page 95
> the recurrence falls into the gap between case 2 and case 3.

Sum of sort algorithm cost
====
insert sort   O(n^2)     O(n^2)  
merge sort    O(nlgn)    O(nlgn)  
heap sort     O(nlgn)    None  
quick sort    O(n^2)     O(nlgn)  
count sort    O(k+n)     O(k+n)  
radix sort    O(dk+dn)   O(dk+dn)  
bucket sort   O(n^2)     O(n)     

prove of cost of bucket sort
----
./readme-time-cost/bucket-sort.rtfd



