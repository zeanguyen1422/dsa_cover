"""A = [1, 2, 3, 4]

return: 3

There are 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself."""

number = [1, 2, 3, 4]

def count_subarray(number):
        count = 0
        count_two = 0 
    
        for i in range(2, len(number)):
    
            
            if number[i] - number[i - 1] == number[i-1] - number[i-2]:
            
                count += 1 
                count_two += count 
            else:
                count = 0 
        return count_two

print(count_subarray(number)) 

