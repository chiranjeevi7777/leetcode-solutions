class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }
        result = 0
        l = len(s)

        for i in range(l):
            current_value = roman[s[i]]
            
            if i < l-1:
                next_value = roman[s[i+1]]
                if current_value < next_value:
                    result -= current_value
                else:
                    result += current_value
            else:
                result += current_value
        return result