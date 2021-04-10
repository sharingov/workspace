class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ans = max(self.helper(s, i, i), self.helper(s, i, i + 1), ans, key=len)
        return ans

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome(input()))
