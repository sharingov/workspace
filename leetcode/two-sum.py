# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = dict()
        for i in range(len(nums)):
            val = d.get(target - nums[i])
            if val is not None:
                return [i, val]
            d[nums[i]] = i
