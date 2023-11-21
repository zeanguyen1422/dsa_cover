
"""Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
These are the 4 subarrays:
1 0 1 0 1 
1 0 1 
1 0 1 0 
  0 1 0 1 
	1 0 1 """


array = [1, 0, 1, 0, 1]
S = 2


def maxSubArray_sum(array, S):
	total_sum = 0 
	total_subarray = 0

	previoustotal_sum = dict()
	previoustotal_sum[0] = 1 # key value 

	for i in range(len(array)):
		total_sum += array[i]

		if total_sum - S in previoustotal_sum: # 0 - 2 in prev? not
			total_subarray += previoustotal_sum[total_sum - S]

		if total_sum in previoustotal_sum:
			previoustotal_sum[total_sum] += 1 
		else:
			previoustotal_sum[total_sum] = 1 
	return total_subarray

print(maxSubArray_sum(array, S))

