# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, left, temp = 0, 0, 0
        d = dict()
        for right in range(len(s)):
            if s[right] in d:
                ans = max(ans, temp)
                n = d[s[right]] + 1
                for i in range(left, n):
                    del d[s[i]]
                    temp -= 1
                left = n
            d[s[right]] = right
            temp += 1
        ans = max(ans, temp)
        return len(s) if len(s) and not ans else ans
