#task: find length of a list
#understand problem size decrease and conquer

#input list l
#output: a number (length of L)

def iter_len(L):
	len = 0
	for x in L:
		len += 1
	return len

#input list l
#output: a number (length of l)
def rec_len(L):
	#take care of irreducible cases(base case)
	if L == []:
		return 0
	else: #reducible case
		first = L.pop(0) 
		return rec_len(L)+1


print(rec_len([10,3,0,5,20]))
