# Iterative maxsum

profits = [-20,50,-30,40,10,5,-50,40]

def maxsum_iterative(L):
	if L==[]:
		return 0
	maxsum = L[0]

	# look at all possible intervals (beg, end)
	for b in range(0, len(L)):
		for e in range(b, len(L)):
			# compute the current sum in this interval from index b to index e
			current_sum = 0
			for i in range(b, e+1):
				current_sum = current_sum + L[i]

			# maintain a maxsum
			if current_sum > maxsum:
				maxsum = current_sum

	return maxsum

for i in range(5):
	profits = (24,18,18,10)
	print(profits, maxsum_iterative(profits))
