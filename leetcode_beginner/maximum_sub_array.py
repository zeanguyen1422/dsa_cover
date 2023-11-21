


# Input: number = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


def maxSubArray(number):

	if number == 1:
		return 1
		
	max_value = number[0]
	current_value = max_value

	for i in range(1, len(number)):

		current_value = max(current_value + number[i], number[i]) 
		max_value = max(max_value, current_value) 
	return max_value


number = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(number))



