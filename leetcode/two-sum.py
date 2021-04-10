class Solution:    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            val = d.get(target - nums[i])
            if val:
                return [i, val]
            d[nums[i]] = i
