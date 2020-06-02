import util
# Maxsum using divide and conquer.

# T(n) = c + c2*n + 2T(n/2) which is = T(n) = n + 2T(n/2) which is n*=
log(n)

def maxsum(L):
	# c steps
	if L==[]:
		return 0
	if len(L) == 1:
		return L[0]

	# break L into Left and Right halves.
	#n steps ; because we slice it
	Left = L[0:len(L)//2]
	Right = L[len(L)//2:len(L)]

	# compute max_sum on Left half
	# T(n/2)
	ms_left = maxsum(Left)

	# compute max_sum on Right half
	# T(n/2)
	ms_right = maxsum(Right)


	# third case: ms overlaping Left and Right
	#c*n
	i = Len(L)//2
	ms_overlap_ending_at_im1 = L[i-1]
	cur_sum = L[i-1]
	for j in range(i-2,-1,-1):
		cur_sum = cur_sum + L[j]
		if cur_sum > ms_overlap_ending_at_im1:
			ms_overlap_ending_at_im1 = cur_sum

	ms_overlap_ending_at_i = L[i]
	cur_sum = l[i]
	for j in range(i+1, len(L)):
		cur_sum = cur_sum + L[j]
		if cur_sum > ms_overlap_ending_at_i:
			ms_overlap_ending_at_i = cur_sum

	ms_overlap = ms_overlap_ending_at_im1 + ms_overlap_ending_at_i

	m = max(ms_left, ms_right, ms_overlap)
	return m

profits = util.random_list(8, -5, 6)
print(profits, maxsum(profits))