#print smallest_of_the_tail#DECREASE & CONQUER
#Task: find a minimum element of a list
#Goal: understand problem size, decrease and conquer 

#input: a list
#output: a number(min item of the list)

def minList(L):
	min = L[0]
	for x in L:
		if x < min:
			min = x
	return min

print(minList([20,15,5,100]))
#Task: find a minimum element of a list
#Goal: understand problem size, decrease and conquer 
#1 Define an API
# output: min element of L 

def my_min(L):
	if L == []:
		print('undefined behahior')
		return
	if len(L) == 1:
		return L[0]
	first = L.pop(0)
	smallest_of_the_tail = my_min(L)
	if first < smallest_of_the_tail:
		return first
	else:
		return smallest_of_the_tail

print(my_min([10,20,15,5,100]))
#2. do some analysis
'''
L = [10, 20, ..., 100]	
first element is 10
L is now equal to [20, ..., 100]
(a)
what if i tell you min element of [20...1000] is 15.
smallest itom of original list is 10.
(b)
what if i tell you min element of [20...1000] is 15.
smallest itom of original list is 5.'''