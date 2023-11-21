
def addtoback(head, newNode):   # addtoback same với append function

    if head is None:    # if not head cl 
        return newNode 
        
    curnode = head 
    
    while curnode:
        if curnode.next == None: 
            curnode.next = newNode 

        curnode = curnode.next # traverse tiếp từng node 

    return head # return linked list

    # create new node mới đâu thì ko có, swe lồn =))) 

# [6] -> [7] -> [8] -> [9] -> 
   
