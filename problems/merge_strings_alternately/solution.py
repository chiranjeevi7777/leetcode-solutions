class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = max(len(word1), len(word2))
        result = ""
        for i in range(l):
            if i < len(word1):
                result += f"{word1[i]}"
            if i < len(word2):
                result += f"{word2[i]}"
        return result
        