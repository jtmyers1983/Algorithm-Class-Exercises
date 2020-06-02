#goal: sort list; divide and conquer
# Input:  A and B are both sorted lists
# Output: C is sorted and is a union of A and B.
def  union(A, B):
	if len(A) == 0:
		return B
	if len(B) == 0:
		return A
	if A[0] < B[0]:
		return [A.pop(0)] + union(A,B)
	return [B.pop(0)] + union(A,B)


#input: two unsorted lists of numbers a & b
#output: a sorted list of numbers, which are the union of a & b
#strategy: use union as a big component of this strategy.
#def sort(a):
	#take care of irreducible case
#	if 
print(sort([1,5,6,10,20,2,4,6,12])	