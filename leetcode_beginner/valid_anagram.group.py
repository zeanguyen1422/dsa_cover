






strs = ["ate","nat","bat", "eat", "tan", "tea"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

import collections 
def function(strs):
    dictionary = collections.defaultdict(list)
    
    for word in strs:
        s = " ".join(sorted(word)) # aet ant abt aet ant aet

        # word = ate nat bat eat tan tea
        
        dictionary[s].append(word)
        
    
    return dictionary.values()



print(function(strs))

