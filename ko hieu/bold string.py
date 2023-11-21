 def addBoldTag(self, s: str, dict: List[str]) -> str:
        marked = [False] * len(s)
        
        for word in dict:
            for j in range(0, len(s) - len(word) + 1):
                if word == s[j:j + len(word)]:
                    for x in range(j, j + len(word)):
                        marked[x] = True
        
        output = []
        
        for i in range(len(s)):
            if marked[i] and (i == 0 or not marked[i - 1]):
                output.append('<b>')
            output.append(s[i])
            if marked[i] and (i == len(s) - 1 or not marked[i + 1]):
                output.append('</b>')
        
        return "".join(output)



""" Time complexity: O(NW). Where N represents the length of string S and W represents the sum of all word lengths.
Space complexity: O(N)). A new array "mask" is used.