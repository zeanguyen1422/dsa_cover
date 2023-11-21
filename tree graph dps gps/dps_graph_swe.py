

# dps with graph 
# hash set 0(1) look up insert delete 

# O(n + e) n is number of nodes , e is number of edges 
# O(n) n is the number of nodes 



class GraphNode:
	def __init__(self, value: int):
		self.value = value 
		self.neigbours = []

	def traverseGraph(cur_node: GraphNode, visited: Set[int]):
		if cur_node is None:
			return 
		if cur_node in visited:
			return 

		visited.add(cur_node)

		print(cur_node.value)

		for i in range(len(cur_node.neigbours)):
			traverseGraph(cur_node.neigbours[i],visited) #recursion cl 
			