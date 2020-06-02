import tree
#input: T, the root, of a binary tree
#output: number of red nodes in the binary tree

def red_nodes(T):
	'''
	idea: number of red nodes in a tree is equal to 
	(a) number of red nodes at the root T, plus
	(b) number of red nodes in the left subtree of T, plus
	(c) number of red nodes in the right subtree of T
	'''
	a, b, c = 0, 0, 0
	if T.data == 'red':
		a = 1
	if T.left is not None:
		b = red_nodes(T.left)
	if T.right is not None:
		c= red_nodes(T.right)
	return a+b+c



t = tree.random_tree(20, colors=['red','g','b'], seed = 42)
tree.draw(t)
print(red_nodes(t))

