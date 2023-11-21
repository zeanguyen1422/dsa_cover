



import collections


# display all adjcecny nodes 

def bfs(graph, root):

	visited = set()
	queue = collections.deque([root])	#dùng queue

	while queue:
		vertexes = queue.popleft()	#remove

		visited.add(vertexes)			#add vô mấy cái remove 
		for i in graph[vertexes]: #value 
			if i not in visited:
				queue.append(i) # rồi tiếp tục vòng loop above
	print(visited)


graph = { 0:[1,2,3],
		  2:[0,1,4], 
		  1:[0,2], 
		  3:[0], 
		  4:[2]}



# tụi nó phải theo thứ tự, layer by layer ko như dps

bfs(graph, 3)


