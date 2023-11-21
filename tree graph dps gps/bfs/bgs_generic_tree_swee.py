




#bfs 

class GenericTree:
	def __init__(self, val):
		self.val = val 
		self.children = []

	def genetricTreeBFS(root):

	queue = deque() and queue.append(root)

	while len(queue) > 0:
		cur_node = len(queue)

		for i in range(cur_node):
			cur_node = queue.popleft()

			print(cur_node.val)

			for child in cur_node.children:
				queue.append(child)


