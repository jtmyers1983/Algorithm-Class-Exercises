

profits = [-20,50,-30,40,10,5,-50,40]

def foo(L):
	for begin in range(0, len(L)):
		for end in range(begin, len(L)):
			print(begin, end)


foo(profits)
# print(util.random_list(10,-10,20))