# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        return [''.join(s)
                for s in product(*[phone[int(i) - 2] for i in digits])]
