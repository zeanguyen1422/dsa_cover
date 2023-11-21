


def parenthesis_generate(n):

	answer = []
	def generate(sofar="", op=0, cl=0):
		if op > n: return # bỏ qua sai
		if cl > op: return # bỏ qua
		if op == cl == n:
			answer.append(sofar)
		generate(sofar + "(", op + 1, cl)
		generate(sofar + ")", op, cl + 1)
	generate()
	return(answer)



print(parenthesis_generate(3))
