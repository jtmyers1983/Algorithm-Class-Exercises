# goal: running time estimation
# running time is proportional to number of "steps" (basic "statements"). 
# running time is proportianl to input size.
# running time is a fucntion of input size. Conventionally input size is denoted as "n".as
# number of steps --> Big O
# we often describe running time of a function as T(n) 
# n : number of items in L (input size)

def my_length(L):   # T(n) = n + 2 steps
	c = 0 			# 1 step
	for x in L:		# n steps (Why? this goes through all items (iterations))
		c += 1		# eash iteration takes 1 step
	return 			# 1 step

print(my_len([3,2,4,5]))

'''
Runnign time of my_len is O(n).
'''
# n : input size (number of items in L)
def f(L):					# T(n) = n^2 + 2
	c = 0					# 1
	for x in L:				# n (iterations, outer loop)
		for y in L:			# n (iterations, inner loop)
			c = c + x + y	# 1
	return 	c				# 1

# unroll the loops. each iteration in the outer loop takes n steps.
# why? because the inner loop takes n steps each time.
# lines 23 -26 take n + n + ... + n or n * n = n^2