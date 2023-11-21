

# bfs dùng với graph và queue 

"""

		A
	B 		C
D	E   F     	G
		  H			I
"""


graph = {
			'A': ['B', 'C'],
			'B': ['D', 'E', 'F'],
			'C': ['G'],
			'D': [],
			'E': [],
			'F': ['H'],
			'G': ['I'],
			'H': [],
			'I': []

}


def bfs(graph, node):

	visited = []
	queue = []

	visited.append(node)
	queue.append(node)

	while queue:
		s = queue.pop(0)
		print(s, end = " ")

		for n in graph[s]: 
			if n not in visited:
				visited.append(n)
				queue.append(n)

print(bfs(graph, "C"))