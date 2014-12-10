part III, data structure
====
Operations on a dynamic set can be grouped into two categories: queries, which simply return information about the set, and modifying operations, which change the set. Here is a list of typical operations. Any specific application will usually require only a few of these to be implemented.

SEARCH(k)
A query that, given a set S and a key value k, returns a pointer x to an element in S such that x:key D k, or NIL if no such element belongs to S.

INSERT(x)
A modifying operation that augments the set S with the element pointed to by x. We usually assume that any attributes in element x needed by the set implementation have already been initialized.

DELETE(x)
A modifying operation that, given a pointer x to an element in the set S, re- moves x from S.(Note that this operation takes a pointer to an element x, not a key value.)

MINIMUM()
A query on a totally ordered set S that returns a pointer to the element of S with the smallest key.

MAXIMUM()
A query on a totally ordered set S that returns a pointer to the element of S with the largest key.

SUCCESSOR(x)
A query that, given an element x whose key is from a totally ordered set S, returns a pointer to the next larger element in S, or NIL if x is the maximum element.

PREDECESSOR(x)
A query that, given an element x whose key is from a totally ordered set S, returns a pointer to the next smaller element in S, or NIL if x is the minimum element.

Content
----
Chapters 10–14 describe several data structures that we can use to implement dynamic sets; we shall use many of these later to construct efficient algorithms for a variety of problems. We already saw another important data structure—the heap—in Chapter 6.


