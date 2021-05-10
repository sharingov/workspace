# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, n: int) -> str:
        s = 'IVXLCDM'
        ans = []
        for i in range(6, -1, -1):
            a = 10 ** (i // 2)
            b = 5 ** (i % 2)
            val = a * b
            if b == 5 and not (n // a + 1) % 5:
                ans.append(s[i - 1] + s[i + (n // a + 1) // 5 - 1])
                n = n % a
            else:
                ans.append(s[i] * (n // val))
                n = n % val
        return ''.join(ans)
