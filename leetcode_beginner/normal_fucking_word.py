class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        
        punction = "!?',;."
    
        for c in punction:
            paragraph = paragraph.replace(c, "")
    
        paragraph = paragraph.lower().split()
    
        hash_map = {}
    
        banned_word = set(banned) # no duplicate 
    
        for pr in paragraph:
    
            if pr in hash_map:
                hash_map[pr] += 1
            else:
                hash_map[pr] = 1
    
        freword = ""
        frecount = 0 
    
        for word, value in hash_map.items():
            if word in banned_word:
                continue
            if value > frecount:
                frecount = value 
                freword = word
        return freword
    
    

