


class Graphnode:
	def __init__(self, val):
		self.val = val 
		self.neigbours = []

	def bfsGraph(starNode):

	queue = deque()
	queue.append(starNode)
	visited = set()

	while len(queue) > 0:
		num_node_layer = len(queue)

		for i in range(num_node_layer):
			cur_node = queue.popleft

			if cur_node in visited:
				continue

			visited.add(cur_node)


			print(cur_node.val)

			for neigbour in cur_node.neigbours:
				if neigbour in visited:
					continue
				queue.append(neigbour)
