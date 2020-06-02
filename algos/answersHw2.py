import tree

#-------------------------------------------------------
# Output: True if all nodes in this tree has 0 or 2 children
def is_good( root_node ):
	# simplest case
	if root_node.left == None and root_node.right == None:
		return True

	# at this point root_node is not a leaf.
	if root_node.left == None and root_node.right != None:
		print(root_node.id, '*')
		return False
	if root_node.left != None and root_node.right == None:
		print(root_node.id, '*')
		return False

	# at this point, both children are not None
	# Logic: root_node is "good" if and only if both
	# left tree and right tree are "good".
	# How: use **the same strategy** on left and right trees.
	return is_good(root_node.left) and is_good(root_node.right)

#-------------------------------------------------------
# t1 = tree.Tree(1, '', None, None)
# t2 = tree.Tree(2, '', None, None)
# t3 = tree.Tree(3, '', t1, None)
# t4 = tree.Tree(4, '', t2, t3)

# print( is_good(t1), 'T' )
# print( is_good(t2), 'T' )
# print( is_good(t3), 'F' )
# print( is_good(t4), 'F' )

# t5 = tree.random_tree(11)
# print( is_good(t5) )
# tree.draw(t5)
#-------------------------------------------------------

# 2.  n is the number of items in the list. n is the problem size.

# 3.

def do_something( L ):			# T(n) = 3 + n*(2+n*(2+n)) = 3 + n*(2 + 2n + n^2) = 3 + 2n + 2n^2 + n^3
	s = 0						# 1
	for x in L:					# n iterations, each iteration takes 2+n(2+n) steps. Loop takes n*(2+n*(2+n))
		s = s + x				#	1
		print(s)				# 	1
		for y in L:				# 	n iterations, each takes 2+n steps.	(The whole loop takes n(2+n) steps)
			s = s + y			#		1
			print(s, x, y)		#		1
			for z in L:			#		n iterations, each takes 1 step. Loop takes n steps.
				s = s + z		#			1
	s = s*5						# 1
	return s 					# 1

# T(n) = 1 + X + 1 + 1 = 3 + X
# X = n*(1 + 1 + Y)
# Y = n*(1 + 1 + Z)

# 4.  T(n) is in O(n^3)
# Why? T(n) = 3 + 2n + 2n^2 + n^3 ≤ 3n^3 + 2n^3 + 2n^3 + n^3  = 8n^3 for n > 1.
# c=3. So, T(n) ≤ 8n^3. Therefore, by defition T(n) is in O(n^3).

# 5

def foo(L):					# T(n) = 1 + X + 1 = 2 + n(1 + 4log2(n))
	s = 0					# 1
	for x in L:				# n iteraations, each takes 1+4*log2(n) steps.  Loop takes n(1 + 4*log2(n))
		j = len(L)			#	1
		while j > 1:		#	log2(n) iterations, each takes 4 steps. Loop takes 4*log2(n) steps.
			j = j / 2		#		1
			s = s + x		#		1
			print(s)		#		1
	return s 				# 1


'''
j		iteration counter
n 		0
n/2		1
n/2^2	2
n/2^3	3
.

n/2^k 	k

loop stops when n/2^k = 1.  So, k = log2(n)


'''