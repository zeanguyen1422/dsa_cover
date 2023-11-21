



# binary tree
# O(n) traverse, where n is number of nodes in binary tree 
# O(logn) binary tree is balanced
# inorder traversal 



class Treenode:
	def __init__(self, value):
		self.value = value 
		self.left = None 
		self.right = None 

	def binary_tree_height(self, root):
		if not root:
			return 0 
		left_height = binary_tree_height(root.left)
		right_height = binary_tree_height(root.right)

		return max(left_height, right) + 1 

