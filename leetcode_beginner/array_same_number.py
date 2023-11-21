
# array [1, 2, 3, 4, 3] True 

def array_check_number(array):

	a = sorted(array, reverse=True)
	for i in range(len(a)):

		j = 1
		if a[i] == a[j] or a[-1] == a [-2]:
			return True
		return False

		j = j + 1


array = [1,5,2,3,4,9,9]
print(array_check_number(array))

