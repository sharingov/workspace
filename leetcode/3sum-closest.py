# https://leetcode.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        le = len(nums)
        for i in range(le - 2):
            left = i + 1
            right = le - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == target:
                    return target
                if val < target:
                    left += 1
                else:
                    right -= 1
                    ans = min(ans, val, key=lambda x: abs(target-x))
                    return ans
