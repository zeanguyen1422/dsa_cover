
# clm dài vl =))) 


class Node:
    def __init__(self, data = None):

        self.data = data
        self.next = None             # khởi tạo value và next 


class linked_list:

    def __init__(self):

        self.head = Node()       # cl

    def append(self, data):

        new_node = Node(data) # create node 
        current_node = self.head   # current pointer
        while current_node.next is not None: #traverse all nodes 
            current_node = current_node.next # traverser each node 

        current_node.next = new_node # assign node hả ko hiểu cái này bên hacker rank cũng làm 

        
        

    # len(linked_list)
    def length(self):

        current_node = self.head
        total = 0
        while current_node.next is not None:
            total += 1 
            current_node = current_node.next 

        return total 

    # print 
    def display(self):

        array = []
        current_node = self.head

        while current_node.next is not None: # iterate all nodes 
            current_node = current_node.next 
            array.append(current_node.data) # append value của từng node một 

        print(array)

    # nhập index biết value [2, 3, 8] index 2 ==> ra value 8
    def get(self,index):

        if index >= self.length() or index < 0: 
            print("ERROR: 'Get' Index out of range!")
            return 

        i = 0
        current_node = self.head
        while True:
            current_node = current_node.next # walk tiếp từng node, walk tiếp từng node 

            if i == index:
            	return current_node.data # 0 <= 2 loop tiếp,return cái value cảu cái cur_node đang loop 

            i += 1 

   		#delete index
    def delete(self , index):

        if index >= self.length() or index < 0: # added 'index<0' post-video
            print("ERROR: 'Erase' Index out of range!")
            return # do nothing 

        i = 0
        current_node = self.head
        while True:
            prev_node = current_node  # ko hiểu
            current_node = current_node.next # walk through từng node 
            if i == index:
                prev_node.next = current_node.next #change pointer, nhưng mà cái code l này ko hiểu 
                		# 2 người kia dùng next next, còn bên đây thêm cái last node
                return

            i += 1 # bên hacker rank với ông kia giải thích hay 


    def prepend_any_index(self, index, data):

        if index >= self.length() or index < 0: # hiểu
            return self.append(data)		# got it 

        current_node = self.head
        prev_node = self.head

        # 2 cái pointer 

        i = 0
        while True:
            current_node = current_node.next # walk through từng node một 
            if i == index: 
                new_node = Node(data) 

                prev_node.next = new_node  
                new_node.next = current_node 

                return 

            prev_node = current_node 

            i += 1

	
    def insert_replace(self, index, data):

        if index >= self.length() or index < 0:
            print("ERROR: 'Set' Index out of range!")
            return

        current_node = self.head
        i = 0
        
        while True:
            current_node = cur_node.next
            if i == index: 
                current_node.data = data #replace value
                return
            i += 1

obj = linked_list()
obj.append(2)
obj.append(3)
obj.append(5)

obj.prepend_any_index(8, 4)
obj.display()