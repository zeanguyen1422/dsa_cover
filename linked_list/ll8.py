

class Node:
   def __init__(self, value=None):
      self.value = value
      self.next = None

class link_list_lồn:
   def __init__(self):
      self.head = None

   def listprint(self):
      cur_node = self.head
      while cur_node is not None: #iterate all nodes 
         print(cur_node.value)
         cur_node = cur_node.next

list = link_list_lồn()
list.head = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.head.next = e2

# Link second Node to third node
e2.next = e3

list.listprint() 

