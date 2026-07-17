class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest_len = len(min(strs, key = len))
        result = ""

        for i in range(shortest_len):
            current_char = strs[0][i]

            for word in strs:
                if word[i] != current_char:
                    return result
            result += current_char
        return result