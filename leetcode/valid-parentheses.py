# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        _list = []
        for i in s:
            if i in '([{':
                _list.append(i)
            elif not _list or abs(ord(i) - ord(_list.pop())) > 2:
                return False
        return not _list
