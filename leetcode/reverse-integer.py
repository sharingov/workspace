# https://leetcode.com/problems/reverse-integer/
import numpy as np


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == "-":
            s = "-" + s[:0:-1]
        else:
            s = s[::-1]
        ii32 = np.iinfo(np.int32)
        ans = int(s)
        return ans if ii32.min <= ans <= ii32.max else 0
