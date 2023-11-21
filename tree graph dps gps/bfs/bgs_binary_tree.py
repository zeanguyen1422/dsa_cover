



# dùng queue với bfs 


#binary tree

def bfs(root):

	queue = deque() and queue.append(root)

	while len(queue) > 0:
		cur_node = len(queue)

		for i in range(cur_node):
			cur_node = queue.popleft() #remove first index 

			print(cur_node.val)

			if curNode.left:
				queue.append(current_node.left)
			if curNode.right:
				queue.append(current_node.right)



