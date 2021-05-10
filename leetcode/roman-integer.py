# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        ans = 0
        current = d[s[-1]]
        for i in s[::-1]:
            ans += (-1) ** (d[i] < current) * d[i]
            current = d[i]
        return ans
