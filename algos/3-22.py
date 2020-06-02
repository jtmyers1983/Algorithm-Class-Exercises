#fibonnaci sequence 0,1,1,2,3,5,8,13,21

#master theroum = T(n) = n^d + a*T(n/b) -> has to be in this form so 
#below is not applicable
#slow fib
def fib1(n):
	if n < 2:
		return n
	else:
		return fib1(n-1) + fib1(n-2)
#T(n) = T(n-1) + T(n-2)
#T(n) >= T(n-1) + T(n-2)
#T(n) >= 2T(n-2) // T(50) >= 2T(48)
#T(n) >= 2T(n-2) > 2^2T(n-4) > 2^3T(n-6)
#T(n) >= 2^(n/2)T(n-n)
#T(n) >= 2^(n/2) = sqrt(2)^n
#slow because it takes at least exponential time
#lots of overlapping

for i in range(10):
	print(i, fib1(i))
'''
use dictionary to store values already computed
Given a function f(x), we want to cache input/output of f.

key is input. value is output of f.
Table[x] stores f(x)

'''
#table[n] stores fib(n)
Table = {}
def fib(n):
	if n in Table:
		return Table[n]
	if n < 2:
		Table[n] = n
		return Table[n]
	else:
		Table[n] = fib(n-1) + fib(n-2)
		return Table[n]

for i in range(50):
	print(i, fib(i))

