


number = [1, 2, 3, 5, 6, 7, 8, 9, 6]

def check_number(number):
	number.sort()
	for i in range(1, len(number)):
		if number[i] == number[i - 1]:
			return True
	return False 




print(check_number(number))

