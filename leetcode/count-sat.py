# https://leetcode.com/problems/count-and-say/
from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        ans = []
        for k, g in groupby(self.countAndSay(n - 1)):
            s = ''.join(g)
            ans.extend([str(len(s)), s[0]])
        return ''.join(ans)
