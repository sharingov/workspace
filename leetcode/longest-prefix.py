# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        pre = strs[0]
        for s in strs:
            for i in range(min(len(s), len(pre))):
                if pre[i] != s[i]:
                    pre = pre[:i]
                    break
            pre = min(s, pre, key=len)
            if not pre:
                return ""
        return pre
