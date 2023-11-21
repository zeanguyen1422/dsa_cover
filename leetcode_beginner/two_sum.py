def two_sumcl(number, target):


	dictionary = {}

	for i in range(len(number)):

		value = number[i] # 3 

		value_find = target - value 

		
		if value in dictionary:
			return (dictionary[value], i) #return cái value của cái key là 1 và cái i đang loop 2 

		if value not in dictionary:
			dictionary[value_find] = i  # {3, 1} 

number = [3, 2, 4]
target = 6

print(two_sumcl(number, target))

