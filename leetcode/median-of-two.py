from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return float(median(nums1 + nums2))

solution = Solution()
print(solution.findMedianSortedArrays(list(map(int, input().split())),
                                      list(map(int, input().split()))))
