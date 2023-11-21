





# used wiih stack (last in first out 
# node visited and node will be visited

# pop khỏi cái stack rồi đánh dấu là cái node đã visited 

# kiểu là add vô rồi remove ra pop ra khỏi stack 



#dfs with graph

from collections import deque

graph = {
			'A': ['B', 'G'],
			'B': ['C', 'D', 'E'],
			'C': [],	
			'D': [],
			'E': ['F'],
			'F': [],
			'G': ['H'],
			'H': ['I'],
			'I': []

}

def dfs(graph, node):
	visited = []
	stack = deque()

	visited.append(node)
	stack.append(node)

	while stack:
		s = stack.pop()
		print(s)

		for n in reversed(graph[s]): #reversed là đảo ngược còn graph[s] là value
			if n not in visited:
				visited.append(n)
				stack.append(n)


"""
			 A
		B 		 G
	C	D  E 	    H
			 F        I
"""

dfs(graph, 'A') 


