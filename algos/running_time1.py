# Running time in terms of O

# T(n) = n + 2.  So, T(n) is in O(n)
# T(n) is in Omega(n)? True.
def f(L):
	s = 0
	for i in range(len(L)):
		s = s + L[i]
	return s

# T(n) = 3n^2 + 2.  So, T(n) is in O(n^2). This is more "tight".
# T(n) is in O(n^4). Also true.  But the bound is not "tight".
# T(n) is in Omega(n)?  True.  Because T(n)=3n^2+1 ≥ 1*n.  Also,
# the loops take at least n steps.
# T(n) is in Omega(n^2)? True.
def g(L):
	s = 0
	for i in range(len(L)):
		for j in range(len(L)):
			s = s + L[i]
			s = s + L[j]
			s = s * L[i] * L[j]
	return s

# g is faster h? Or h is faster than g?  h is faster than g.
# T(n) is in O(n^3).  True.
# T(n) is in O(n^2).  True. Why? Intuitive reason: h is faster than g.
# and r.t of g is in O(n^2.)
# What if we don't have g.
# T(n) = 2 + n * (at most n)
# T(n) ≤ 2 + 3n^2 ≤ 5n^2.  Therefore, T(n) is in O(n^2).
#
# Is O(n^2) tight?
# Is T(n) in Omega(n)?  T(n) ≥ 1*n.  Why?  outer loop.
# Is T(n) in Omega(n^2)?  True.
# T(n) is in Theta(n^2).  O and Omega have the same bound.
def h(L):
	s = 0
	for i in range(len(L)):
		for j in range(i, len(L)):
			s = s + L[i]
			s = s + L[j]
			s = s * L[i] * L[j]
			print(i,j)
	return s

h([1,2,3,4,5])
