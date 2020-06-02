
xT(n) is the running time of some function.
n is the input size.  T is a function of input size.
For example, T(n) = 5n + 3.  This is an estimate of running time in terms
of *exactly* the number of steps.

Problem: it is not ok to be able to estimate exactly the number of steps.
Some step takes more time than another step.

A solution: T(n) = an + b, where a and b are some numbers greater than 0.

We can further simplify this situation, using asymptotic complexity (i.e Big-O).

For example, we say 5n+3 is in O(n).

Here's the math definition.

f(n) is in O(g(n)) if f(n) ≤ c * g(n), for some number c > 0, for all values of n large enough.

5n+3 is in O(n) because 5n+3 ≤ 8*n when n is large enough.
(Here, c = 8.)

10n + 5n^2 + 3 ≤ 18n^2, for all values of n > 1.
Therefore, 10n+5n^2+3 is in O(n^2). (c = 18)

Exam #1 is on Feb 22, 2018.

5n^2 + 10 is in O(n^3). True because 5n^2 + 10 ≤ 5n^3 + 10n^3 for all n > 1.
Therefore, 5n^2 + 10 is in O(n^3).  We found c to be 15.

====

Understanding Big O.

- O is an estimate of running time. Asymptotic complexity.
- Very roughly speaking, O ignores constants.
- O is un upper bound.  Not an exact bound.

T(n) is in O(n^3) means intuitively T(n) is at most order of n^3, and mathematically T(n) < c*n^3 for large values of n.

- Order of n^3 means:  c*n^3
- O(n^3) is a set of functions. { 150n, 20, 5n+10, 20n^2-5, 20n^3, ... }
- 5n^4 is not in O(n^3).
- n^3.1 is not in O(n^3)

8n+5n^2-100 is in O(n^2).
Why? 8n+5n^2-100 ≤ 13n^2 for all n > 1. c=13.

================
Omega


f(n) is in O(g(n)) if f(n) ≤ c * g(n), for some number c > 0, for all values of n large enough.

f(n) is in Omega(g(n)) if f(n) ≥ c * g(n), for some number c > 0, for all values of n large enough.

O specifies an upper bound.

Omega specifies a lower bound.

- Is 5n + 10 in O(n)? True
- Is 5n + 10 in Omega(n)? True.  5n+10 is at least order of n.

5n + 10 ≥ 1*n for all n > 1.

- Is 5n^2 + 10n in Omega(n^2)?  True.

5n^2 + 10n ≥ 1*n^2 for n>1

- Is 5n^2 + 10n in Omega(n)? True

True:   5n^2 + 10n ≥ 1*n for n > 1.


















