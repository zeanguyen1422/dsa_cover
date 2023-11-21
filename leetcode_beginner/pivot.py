





def find_index(array):

	left = 0
	total_sum = sum(array)

	for i, right in enumerate(array):
		total_sum_right = total_sum - right
		if left == total_sum_right:
			return i 
		left += right #array = [1, 2, 8, 5, 2, 9] 
	return -1


array = [1, 2, 8, 5, 2, 9]
print(find_index(array))

# return index của 5 vì 5 là pivot 	