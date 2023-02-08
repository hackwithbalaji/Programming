class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1 ,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0 
        res = 0
        while i < len(s):
            current_char = s[i]
            if i+1 < len(s):
                next_char = s[i+1]
                if roman[current_char] < roman[next_char]:
                    res = res - roman[current_char]
                else:
                    res = res + roman[current_char]
            else:
                res = res + roman[current_char]
            i = i+1 
        
        return res