# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from bisect import bisect_right, bisect_left


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        i = bisect_left(nums, target)
        if i == len(nums) or nums[i] != target:
            return [-1, -1]
        j = bisect_right(nums, target)
        return [i, j - 1]
