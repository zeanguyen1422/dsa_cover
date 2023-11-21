


def same_number_check(number_input):

    if number_input < 0:
        return False


    temp = number_input
    reversed_number = 0 

    while temp != 0:
        digit_store_value = temp % 10
        reversed_number = reversed_number * 10 + digit_store_value 
        temp = temp // 10 

    return reversed_number == number_input  

  


print(same_number_check(212))