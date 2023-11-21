
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freq = dict()
        bannedSet = set(banned)

        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        words = paragraph.lower().split()

        for word in words:
            if word not in freq:
                freq[word] = 0

            freq[word] += 1

        maxCount = 0
        mostFreqWord = ""

        for word, count in freq.items():
            if word in bannedSet:
                continue

            if count > maxCount:
                maxCount = count
                mostFreqWord = word

        return mostFreqWord