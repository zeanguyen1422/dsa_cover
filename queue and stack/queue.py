
# insert and delete dùng queue


# insert = enqueue 
# delete = dequeue 


# first in first out 
# xếp hàng á 

# used for bfs deal with graph tree 
# shortest path beetween 2 nodes in a graph 
# traversing a tree level by level




from collections import deque

queue = deque()

queue.append(8)
queue.append(12) # O(1)


print(queue.popleft())	# O(1)


print(queue)


