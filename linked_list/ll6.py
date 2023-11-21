
class Node:
	def _init_(self, data):
		self.item = data 
		self.ref = None  # same với ref 

class Linklist:
	def _init_(self):
		self.head = None


	def insert_at_start(self, data):
		new_node = Node(0) # cái data

		new_node.ref = self.head # reference lại first node, giống với bên hacker rank
		# clm mấy app vẽ tích hợp vô web app của mình
			
		self.head = new_node # change the head poitner lại cái new_node 
		# hacker rank giải thích hay vl 


									

	def traverse(self):
		if self.head is None:
			print("Linked list is empty")
			return 
		else:
			current = self.head 
			while current is not None:
				print(current.item, " ")
				current = current.ref # nó dùng temp mình thích lấy là current hơn 

	def delete(self, data): # cái này ko phải delete cái index nha mà delete hẳn cái data muốn delete luôn

		# nếu data là head muốn delete ấy 
		temp = self.head 
		if self.head.item == data: # data muốn delete 
			self.head = self.head.ref # pointer tới ref mới 
			return 

		while temp is not None:
			if temp.ref.item == data: # data you want to delete, ref là next 
				break 
			# 3 dòng code trên mình hiểu rồi break là true khi đúng data mình muốn delete 

			temp = temp.ref # walk tiếp 
			

			if temp.ref is None:
				print("None")

				#   temp    ref    ref 	
			else: # [3] -> [5] -> [8] 
				temp.ref = temp.ref.ref # giống bên hacker rank
				


# object of linklist
new_link_list = Linklist()

# new_link_list.insert_at_start(1)