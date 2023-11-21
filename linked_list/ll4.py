
# hacker rank chị này so good 

		# value 
# head, current, current next, current nextnext 



class Node:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next # next value và data

class Linkedlist: # playaround with class Node 


	def append(self, data): 
		if head is None:
			head = Node(data) # head is none thì create cho nó thôi 
			return

		current = head 
		while (current.next is not None): # walk through linked_list 
			current = current.next # walking 

		current.next = Node(data) # the end of linked list, create new node, cái này chưa hiểu lắm =))) 


	def prepend(self, data): 
		new_head = Node(data) # create new node value 
		new_head.next = head # link [new_head.next] -> [head]
		head = new_head # change the head pointer    [new_head.next] <- [head]

	def delete_value(data):
		if head is None:
			return # nothing to do 

		if head.data == data: # data you want to delete 
			head = head.next # pointer to cái tiếp theo hiểu hiểu 
			return 

		current = head # current tiếp để walk through the linked list 

		while (current.next is not None): # walking
			if current.next.data == data: # the data you want to delete, data same với value whatever call 

				current.next = current.next.next # next value pointer tới cái tiếp theo nữa hiểu hiuể 
				return # return 

			current = current.next # move on 

