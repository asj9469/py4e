# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        if len(s) == 1:
            return dic[s]

        i = 1
        num = 0
        while i < len(s) + 1:
            n = 0 if i == len(s) else dic[s[i]]
            if n <= dic[s[i - 1]]:
                num += dic[s[i - 1]]
            else:
                num += n - dic[s[i - 1]]
                i += 1
            i += 1

        return num