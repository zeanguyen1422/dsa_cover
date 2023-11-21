




def find_index_pivot(array):

	
	total_sum = 0 
	for i in range(len(array)):
		total_sum += array[i]	

	left = 0 

	for i in range(len(array)):
		right = total_sum - array[i] - left 	
														#left += array[i]	để trên đây thì cái left nó add tới cái total_sum luôn 
		if left == right:
			return i

		else:
			left += array[i]	# nó + tới 11 --> cập nhật cái này ở đây nè 
	
	return - 1 


array = [1, 2, 8, 16, 7, 4]	
		
print(find_index_pivot(array))


	
	