


# graph
# dfs 


graph = {
	'A': ['B', 'C', 'D'], 'B':['E'], 'C':['D','E'], 'D':[], 'E':[]
	}

#output là A B E C D 

visited = set()

def dfs(visited, graph, root):
	if root not in visited:
		print(root)
		visited.add(root)
		for neigbour in graph[root]:	#lấy value
			dfs(visited, graph, neigbour)	#recursion

dfs(visited, graph, 'A')



