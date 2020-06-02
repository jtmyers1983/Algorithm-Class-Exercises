# Goal: running time estimation

def foo(L):					# T(n) = 3n^2 + 3
	s = 0					# 1
	for x in L:				# n iterations, each takes 3n steps. Loop takes n*3n steps
		for y in L:			#		n iterations, each takes 3 steps. Loop takes n*3
			s = x + s		#				1
			s = y + s		#				1
			print(s)		#				1
	s = 5 * s				# 1
	return s				# 1

# 1. estimate EXACTlY the number of steps:  T(n) = 3n^2 + 3
# 2. estimate using "non-specific" constants:  T(n) = an^2 + b


# sum of list
def my_sum(L):							# T(n) = 7 + T(n-1)
	if L==[]:							# 1
		print('undefined behavior')		# 1
		return 							# 1
	if len(L) == 1:						# 1
		return L[0]						# 1
	first = L.pop(0)					# 1
	return first + my_sum(L)			# 1 (addition) + T(n-1)

'''
1. We don't know  # of steps of the recursive.
2. T(n) is a function of n, which is the number of items of the original input.
3. T(n) is the number of steps of my_sum for a list with n items.
4. Line 18, the r.t of my_sum for a list w. n-1 items is T(n-1)


T(n) = 7 + T(n-1)
	 = 7 + ( 7 + T(n-2) ) 					since T(n-1) = 7 + T(n-2)
	 = 7 + 7 + ( 7 + T(n-3) )				since T(n-2) = 7 + T(n-3)
	 = 7 + 7 + 7 + ... + 7 
	 = 7n

'''
