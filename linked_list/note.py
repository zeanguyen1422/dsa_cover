


# linked list 

#linear order
# head data next tail (singly linked list
# head prev data next tail ( double linked list 
# circular linked list 
# used linked list with stack and queue

# 	prev	data(value)		next 



class Node:
	def _init_(self, data):
		self.data = data 
		self.next = None 
		self.prev = None 

class LinkedList:
	def __init__(self):
		self.head = None 