# https://leetcode.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: list[int]):
        le = len(nums)
        p = le - 2
        while nums[p] >= nums[p + 1]:
            p -= 1
            if p == -1 or p == -2:
                nums[:] = nums[::-1]
                return
        re = p + 1
        while re < le - 1 and nums[re + 1] > nums[p]:
            re += 1
        nums[p], nums[re] = nums[re], nums[p]
        nums[p + 1:] = nums[:p:-1]
