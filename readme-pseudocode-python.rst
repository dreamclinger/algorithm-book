pseudo-code in book
====
for j = 2 to A.length   
    key = A[j]
    //Insert A[j] in to the sorted sequence A[1,2,...j-1].
    i = j - 1
    while i > 0 and A[i] > key
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

real-code in python, notice the index begins from 0, not 1
====
for j in range(1,len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
