class Solution:
    def romanToInt(self, s: str) -> int:
        
        value = 0
        romanValues = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,

        }

        for x in range(len(s) - 1):
            if romanValues[s[x]] < romanValues[s[x+1]]:
                value -= romanValues[s[x]]
            else:
                value += romanValues[s[x]]
            
        return value + romanValues[s[-1]]
