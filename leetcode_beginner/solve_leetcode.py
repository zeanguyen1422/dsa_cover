
"""
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4

"""


array = [[1,2,3],
 [4,5],
 [1,2,3]] # len(array) = 3 


def cl(array):

    if len(array) == 0:
        return 0 

    max_so_far = array[0][-1]
    min_so_far = array[0][0]

    max_value = 0

    for i in range(1, len(array)):

        loop_array_value = array[i]
        cur_max = loop_array_value[-1] # loop inside dùng cái variable ở trên 
        cur_min = loop_array_value[0]

        max_value = max(max_value, abs(cur_max - min_so_far), abs(max_so_far - cur_min))

        min_so_far = min(min_so_far, cur_min)
        max_so_far = max(max_so_far, cur_max)

        # update rồi 2 lần loop 1 2 

    return max_value 


print(cl(array))


