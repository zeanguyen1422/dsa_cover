







# def firstUniqChar(self, s: str) -> int:

def firstUniqChar(s):
    
    freqMap = dict()

    for i in range(len(s)):
        if s[i] not in freqMap: #key
            freqMap[s[i]] = 0 # assgin value
        freqMap[s[i]] += 1 # increment value
        

    for i in range(len(s)):
        if freqMap[s[i]] == 1:
            return i   # cái i thôi nó đêm1 index 

    return -1

    


s = "swecareers"

print(firstUniqChar(s))