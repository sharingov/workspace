# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, h: list[int]) -> int:
        left, right = 0, len(h) - 1
        ans = 0
        while left < right:
            ans = max(ans, (right - left) * min(h[left], h[right]))
            if h[left] < h[right]:
                left += 1
            else:
                right -= 1
        return ans
