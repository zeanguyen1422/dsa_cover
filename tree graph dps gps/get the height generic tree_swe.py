






# binary tree
# O(n) traverse, where n is number of nodes in binary tree 
# O(logn) binary tree is balanced
# inorder traversal 



class GenericTree:
	def __init__(self, value):
		self.value = value 
		self.children = []

	def generic_tree_height(self, root):
		if not root:
			return 0 

		max_height = 0
		for i in range(len(root.children)):
			childheight = generic_tree_height(root.children[i])
			max_height = max(childheight, max_height)

		return max_height + 1 


