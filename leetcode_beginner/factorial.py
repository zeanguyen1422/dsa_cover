



	
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def factorail(n):

	terms = [0, 1]		
	i = 2 
	while i <= n:
						# terms[0]	+    terms[1] --> terms[1] + terms[2] --> terms[2] + terms[3]
		terms.append(terms[i-2] + terms[i - 1])
		i += 1 

	print(terms)
	return terms[n]



print(factorail(5))



