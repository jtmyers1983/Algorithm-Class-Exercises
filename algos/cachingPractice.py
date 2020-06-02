# Practice caching
table = {}
def foo(n):
	global table
	
	if n in table:
		return table[n]
	if n == 0:
		table[n] = 5
		return table[n]
	if n == 1:
		table[n] = 10
		return table[n]
	if n == 2:
		table[n] = 20
		return table[n]
	table[n] = foo(n-1) + foo(n-2) + foo(n-3)
	return table[n]

#-------------------------------------
for i in range(50):
	print(i, foo(i))