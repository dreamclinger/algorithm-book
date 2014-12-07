pseudo-code in book, e.g. insert-sort
====
for j = 2 to A.length   
    key = A[j]
    //Insert A[j] in to the sorted sequence A[1,2,...j-1].
    i = j - 1
    while i > 0 and A[i] > key
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

real-code in python, e.g. insert-sort.py
====
for j in range(1,len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

list of different implements in python compared to the book
====

index
----
[0,...]

range(a,b)
----
[a,b)

insertsort(A)
----
assume you pass the address of list, then A itself is revised in the function. you don't need to return anything in function insertsort

basic operas in python for supporting pseudocode
====

float("inf")
----
#largest number

L.append(A[i])
----
#add key = A[i] to L[]

math.floor / ceil
----
#get integer

