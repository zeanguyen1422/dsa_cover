



def removeDuplicates(number):
	j = 1
	for i in range(1, len(number)):
	    if number[i] != number[i - 1]:
	        number[j] = number[i]
	        j += 1




number = [0,0,1,1,1,2,2,3,3,4]

# 0 1 2 3 4 
print(removeDuplicates(number))

