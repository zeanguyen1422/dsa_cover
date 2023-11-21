




number = [1, 2, 3, 4, 5, 8, 10, 12]

# [1, 2, 3]
# [1, 2, 3, 4]
# [2, 3, 4]

# output là 3 


def numbera(number):

    count = 0
    count_two = 0 

    for i in range(2, len(number)):

        
        if number[i] - number[i - 1] == number[i-1] - number[i-2]:
        
            count += 1 
            count_two += count 
        else:
            count = 0 
    return count_two


print(numbera(number))

