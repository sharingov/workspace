from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int):
        d = {}
        for a, b in logs:
            d.setdefault(a, set()).add(b)
        l = [0 for i in range(k)]
        for v in d.values():
            l[len(v) - 1] += 1
        print(l)

sol = Solution()
sol.findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]], 5)
