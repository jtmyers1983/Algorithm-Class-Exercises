# Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

# Table[n] stores fib(n)
Table = {}
def fib(n):
	if n in Table:
		return Table[n]

	if n < 2:
		Table[n] = n
		# return n
		return Table[n]
	else:
		Table[n] = fib(n-1) + fib(n-2)
		# return fib(n-1) + fib(n-2)
		return Table[n]

#-----------------------------------------------------
def slow_fib(n):
	if n < 2:
		return n
	else:
		return slow_fib(n-1) + slow_fib(n-2)

#-----------------------------------------------------
def iterative_fib(n):
	table = {}
	table[0] = 0
	table[1] = 1
	for i in range(2,n+1):
		# table[i] stores fib(i)
		table[i] = table[i-1] + table[i-2]
		# table[i] = iterative_fib(i-1) + iterative_fib(i-2)
	return table[n]

#-----------------------------------------------------
def another_fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = a + b, a
	return a

#-----------------------------------------------------

for i in range(50):
	print(i, fib(i), iterative_fib(i), another_fib(i))


'''
Caching

Given a function f(x), we want to cache input/output of f.
How?  Answer: Have a dictionary/hash to store output of f.
Key is input of f.  Value is output of f.
Table[x] stores f(x)


'''