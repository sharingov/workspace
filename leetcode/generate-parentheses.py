# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(sub=[], left=0, right=0):
            if len(sub) == n * 2:
                ans.append(''.join(sub))
                return
            if left < n:
                sub.append('(')
                backtrack(sub, left + 1, right)
                sub.pop()
            if right < left:
                sub.append(')')
                backtrack(sub, left, right + 1)
                sub.pop()
        backtrack()
        return ans
