# https://leetcode.com/problems/combination-sum/
from collections import Counter


class Solution:
    def combinationSum(self, candidates: list[int], target: int):
        candidates = sorted(candidates)
        ans = []

        def func(base, cur):
            for i in candidates:
                if cur + i > target:
                    return
                if cur + i < target:
                    func(base + [i], cur + i)
                else:
                    c = sorted(Counter(base + [i]).elements())
                    if c not in ans:
                        ans.append(c)
                    return

        func([], 0)
        return ans
