


# left to right
# binary tree
# dùng nó với stack add và pop 

# last in first out 


# just a concept and m phải biết rõ syntax của programming language m dùng


class Node:
	def __init__(self, value):
		
		self.value = value 
		self.left = None 
		self.right = None 


#recursion
def traverse_tree(tree):
	if tree is not None:
		print(tree)
		traverse_tree(tree.left)
		traverse_tree(tree.right)

		# root left right 


#iterative
def traverse_tree2(tree, stack):

	stack.append(tree)
	while len(stack) > 0: # loop tiếp right, left kiểu v mình nghĩ v 
		node = stack.pop()
		if node is not None:
			print(node)
			stack.append(node.right) # append rồi loop ở trên k
			stack.append(node.left)

			#root right left 
			# kiểu add root rồi remove nó, print nó ra 




