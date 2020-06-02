def sum_list(L):
	#initialize s
	s = 0

	# go through each item of L and add it to s
	for i in L:
		s = s + i
	return s

print(sum_list([1,2,3]), 'should be equeal to 6.')
