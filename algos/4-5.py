# 1 (if objects are not orderable and not hashable)
# here's an Theta(n^2)
def iterative_majority(L):
	most_freq_item, f = None, 0
	# count freq of each item and keep track of highest freq

	for item in L:
		# count freq of item
		fx = 0
		for x in L:
			if x == item:
				fx += 1

		# keep track of most freq item
		if fx > f:
			most_freq_item, f = item, fx

	if f > len(L)/2:
		return most_freq_item
	return None

#-----------------------------------------------------------
# 1 (if objects are not orderable but is hashable)
# here's an Theta(n), assuming freq[item] takes c steps.
def iterative_majority(L):
	freq = {}
	for item in L:
		if item not in freq:
			freq[item] = 0
		freq[item] += 1
		if freq[item] > len(L)//2:
			return item
	return None

#-----------------------------------------------------------
'''
Problem 3
- Divide L into two halves.
-
'''

def majority_dc(L):
	if L==[]:
		return None
	if len(L) == 1:
		return L[0]
	Left = L[0 : len(L)//2]
	Right = L[len(L)//2 : len(L)]
	m_left = majority_dc(Left)
	m_right = majority_dc(Right)

	f_left = 0
	for x in L:
		if m_left == x:
			f_left += 1
	if f_left > len(L)//2:
		return m_left

	f_right = 0
	for x in L:
		if m_right == x:
			f_right += 1
	if f_right > len(L)//2:
		return m_right

	return None


# T(n) = c*n + 2T(n/2).  T(n) is in Theta(n log n)


# Problem 5
Costs =   	[24, 10, 10, 7]
Profits = 	[24, 15, 15, 11]
Budget = 24

def greedy_invest(T, costs, profits):
	pc_ratio = []
	for i in range(len(costs)):
		pc_ratio.append((profits[i] / costs[i], profits[i], costs[i]))
	pc_ratio.sort(reverse=True)
	best_profit = 0
	current_budget = T
	for i in range(len(pc_ratio)):
		if current_budget <= 0:
			break
		if current_budget >= pc_ratio[i][2]:	#have enough money to invest in this item
			current_budget -= pc_ratio[i][2]	#take this item
			best_profit += pc_ratio[i][1]		#record the profit
			print('Take item with cost {} and profit {} Current budget: {}'.format(pc_ratio[i][2],pc_ratio[i][1], current_budget))
	return best_profit



print(greedy_invest(Budget, Costs, Profits))