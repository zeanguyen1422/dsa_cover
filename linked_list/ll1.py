

# itereate
# keep track of previous node để nó assign khi delete node 

# [6] -> [7] -> [8] -> [9] ->
# [6] -> [7] ->        [9] -> 
# O(n) where n is the size of linked list 

# swe lồn =))) 

class Node:
    def _init_(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next # pointer to next node nè 
        self.prev = prev # pointer về sau doubly linked list 

    def traverse_linked_list(head, index):

        head = Node(val)            # value hay data đều được 
        prev_node = None 
        cur_node = head 

        cur_count = 1

        if not head:
            return head 

        if index < 1:
            return head   # mấy cái này hình như là trong 1 function tìm index thôi 

        # remove head node rồi pointer to next node     
        if index == 1:
            second_node = head.next 
            head.next = None 
            return second_node   # ko hiểu mấy dòng code này 

        while cur_node is not None:
            if cur_count == index: # tìm index muốn delete
                prev_node.next = cur_node.next   # ko hiểu
                cur_node.next = None # ko hiểu =)))
                return head                 

            prev_node = cur_node #prev_node trong doubly linked list, chắc walk tiếp 
            print(cur_node.val) 
            cur_node = cur_node.next # walking tiếp
            cur_count += 1                 

        return head 

