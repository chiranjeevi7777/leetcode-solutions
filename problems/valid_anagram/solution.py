class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            False
        freq_t = {}
        freq_s = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1
        for ch in s:
            freq_s[ch] = freq_s.get(ch, 0) + 1
        return freq_t == freq_s
            
        