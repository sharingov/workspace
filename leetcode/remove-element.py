# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == val:
                nums.pop(i)
            i += 1
        return len(nums)
