
# itereate through the linked list dùng index nhập á

def link_list_find_index(head: Node, index: int) -> Node:

   if not head:
      return None

   if index < 1:
      return None  # cái này ko hiểu 

   cur_count = 1 
   cur_node = head 

   while curnode:
      if cur_count == index: # nếu mà nhập index = 1 thì nó trả về liền luôn 
         return cur_node

      cur_node = cur_node.next # walk 
      cur_count += 1 

   return None # > size link list return None 


# [6] -> [7] -> [8] -> [9] -> [10]
# nếu mà index = 6 thì outside of linked list thì return none 

# O(n) where n is the size of linked list
