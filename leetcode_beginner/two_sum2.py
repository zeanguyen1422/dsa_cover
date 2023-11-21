





# number = [2, 11, 8, 9]



def two_sum(number, target):

	

	for i in range(len(number)):
		for j in range(i+1, len(number)):
			if number[i] + number[j] == target:
				return i, j 
	return -1 




number = [2, 11, 8, 9] 
print(two_sum(number, 19))

 
