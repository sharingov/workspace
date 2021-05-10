# https://leetcode.com/problems/divide-two-integers/
class Solution:
    def divide(self, a: int, b: int) -> int:
        ans = 0
        neg = (a < 0) is not (b < 0)
        a, b = abs(a), abs(b)
        while a >= b:
            temp, i = b, 1
            while a >= temp:
                a -= temp
                ans += i
                i <<= 1
                temp <<= 1
        if neg:
            ans = -ans
        return min(2147483647, ans)
