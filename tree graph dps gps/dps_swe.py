






# binary tree
# O(n) traverse, where n is number of nodes in binary tree 
# O(logn) binary tree is balanced
# inorder traversal 


#binary search tree left tree nodes < right tree nodes 
# binary search tree is balanced thì O(logn) for search, insertion, deletion compare to array, linked list searching is O(N)  


class Treenode:
	def __init__(self, value):
		self.value = value 
		self.left = None 
		self.right = None 

	def print_binary_tree(self, root):
		if not root:
			return 0 
		print_binary_tree(root.left) 	#recursion
		print(root.value)
		print_binary_tree(root.right) 

