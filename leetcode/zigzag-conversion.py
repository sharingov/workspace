# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        _list = []
        val = 2*(n-1)
        for i in range(n):
            j = i
            b = True
            while(j < len(s)):
                _list.append(s[j])
                j += val - (2 * i) % val if b else val - (val - 2 * i) % val
                b = not b
        return ''.join(_list)
