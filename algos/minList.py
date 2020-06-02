#Task: find a minimum element of a list
#Goal: understand problem size, decrease and conquer 
#1 Define an API
# output: min element of L 

def my_min(L):
	if L == []:
		print('undefined behahior')
		return
	if len(L) == 1:
		return L
	first = L.pop(0)
	print(first)
	
	smallest_of_the_tail = my_min(L)

	if first < smallest_of_the_tail:
		return first
	else:
		return smallest_of_the_tail


print(my_min([10,5,20,7,10]))