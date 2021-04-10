def fourSum(nums: list[int], target: int) -> list[list[int]]:
    ans = []
    nums.sort()
    le = len(nums)

    for i in range(le - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, le - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            l = j + 1
            r = le - 1
            while l < r:
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    ans.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
    return ans
