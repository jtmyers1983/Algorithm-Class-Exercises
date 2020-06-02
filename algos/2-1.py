# Goal: running time estimation
#
# running time is proportional to number of "steps" (basic "statements").
# running time is proportional to the input size.
# running time is a function of input size.  Conventionally, input size is denoted as "n".
# we often describe/define running time of a function as T(n)
# number of steps --> Big O

#---------------------------------------------
# n : number of items in L (input size)
def my_len(L):					# T(n) = n + 2
	c = 0						# 1 step
	for x in L:					# n steps  (Why? this goes through all items (iterations))
		c += 1					#		(each iteration takes 1 step)
	return c 					# 1 step

#---------------------------------------------
# n : input size (number of items in L)
def f(L):							# T(n) = 2n^2 + 2
	c = 0							# 1
	for x in L:						# this has n iterations
		for y in L:					# each iteration takes 2n
			c = c + x + y			#
			c = c * 10				#
	return c 						# 1

'''
T(n) = an^2 + b

Outer loop (line 21) has n iterations.  Each iteration is the inner loop.
Inner loop (line 22) has n iterations.  Each iteration takes 2 steps.
n*2n = 2n^2

'''
# unroll the loops. Each iteration in the outer loop takes n steps.
# Why? because the inner loop takes 2n steps each time.
# Lines 21-24 take 2n + 2n + ... + 2n or n*n = 2n^2.

#---------------------------------------------
def g(L):				# T(n) = 2n + 3
	s = 0				# 1
	i = 0				# 1
	while i < len(L):	# n iterations, each takes 2.
		s = s + L[i]	# 1
		i += 1			# 1
	return s 			# 1
'''
T(n) = an + b

i   	iteration
0		1
1		2
2		3
.
.
n-1		n
--> Therefore, the loop (line 41) take n iterations.
'''
#---------------------------------------------
def h(L):				# T(n) = 2*(log2(n)+1) + 3
	s = 0				# 1
	i = 1				# 1
	while i < len(L):	# log2(n) + 1 iterations
		s = s + L[i]	# 1
		i = i*2			# 1
	return s 			# 1

T(n) = a*log(n) + b

'''
i 		iteration
1					1
2					2
2^2					3
2^3					4
2^4					5
2^5		 			6
.
.
2^(K-1) = n  		K
Therefore, the loop (line 59) takes log2(n) + 1 iterations.


for i in range(len(L)):			# n iterations
	j = 1						# 1
	s = 0						# 1
	while j < len(L):			# log2(n)+1 iterations
		j = j * 2
		print(s)
	for x in L:					# n iterations
		s = s + x
		s = s + 5
		print(s)

Total # of steps: n*(2 + (log2(n)+1)*2 + n*3)
'''
# SO FAR, WE ESTIMATE R.T. BY COUNTING EXACTLY NUMBER OF STEPS.

def h(L):				# T(n) = 3*(log2(n)+1) + 8
	s = 0				# 1
	i = 1				# 1
	while i < len(L):	# log2(n) + 1 iterations
		s = s + L[i]	# 1
		s = s*20
		print(s)
		i = i*2			# 1
	s = 10 * s**5		# 1
	s = 10 * s**5		# 1
	s = 10 * s**5		# 1
	s = 10 * s**5		# 1
	s = 10 * s**5		# 1
	return s 			# 1

'''
equal sign (line 93) is a problem.
we can't say T(n) is EXACTLY that.
T(n) = a*log(n) + b.  T(n) is in ϴ(log(n)).
where a, b, c are constants.

ϴ - Theta
ϴ(log(n)) is the set of functions { a*log(n) + b }, a > 0, b > 0
ϴ(n) is the set of functions { a*n + b }.


What is O(n)?
O(n) is the set of functions that have r.t greater than or equal n.

+ O is a measure.
+ O(n) is a set of functions.
+ O(log n) is a set of functions.
+ O(n^2) is a set of functions.
+ O(n) = { 10n, 5n+20, 6n-10, 0.5n + 20, .... }
+ O(n^2) = { n^2, 2n^2, 0.005n^2 + 100, }
+ Is 5n in O(n^2)?  Yes?

'''




