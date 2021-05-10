# https://leetcode.com/problems/4sum/
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans = []
        nums.sort()
        le = len(nums)

        for i in range(le - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, le - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = le - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return ans
