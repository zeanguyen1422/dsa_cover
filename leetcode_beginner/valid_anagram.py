

# Input: s = "anagram", t = "nagaram"
# Output: true 



def function(s, l):

	s = sorted(s)
	l = sorted(l)

	if s == l:
		return True
	return False


s = "anagram"
l = "nagaram"
print(function(s,l))

