





number = [1, 2, 3, 5, 6, 7, 8, 9, 6]

def check_number(number):

	if len(number) == len(set(number)):	
		return False
	return True




print(check_number(number))


