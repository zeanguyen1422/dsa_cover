








array = [3, 3, 3, 3, 5, 5, 5, 8, 8, 8, 3, 3, 3, 3] # hiều rồi 


# maximum number array check > len(n) chia 2 
# majority element


def cl(array):

	n = len(array)
	dictionary = {}

	for i in array:
		dictionary[i] = dictionary.get(i, 0) + 1

	n = n // 2
	for key, value in dictionary.items():
		if value > n:
			return key 
	return 0 



print(cl(array))



		
