# https://leetcode.com/problems/median-of-two-sorted-arrays/
from statistics import median


class Solution:
    def findMedianSortedArrays(
            self, nums1: list[int],
            nums2: list[int]) -> float:
        return float(median(nums1 + nums2))
