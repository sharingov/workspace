# https://leetcode.com/problems/3sum/
from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        le = len(nums)
        d = defaultdict(list)
        ans = set()

        for i in range(le):
            for j in range(i):
                d[nums[i] + nums[j]].append((j, i))

        for i in range(le):
            for a, b in d.get(-nums[i], [(0, 0)]):
                if a != b and a != i and b != i:
                    ans.add(tuple(sorted((nums[a], nums[b], nums[i]))))
            d.pop(-nums[i], None)

        return list(list(i) for i in ans)
