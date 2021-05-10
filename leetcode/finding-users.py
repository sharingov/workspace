# https://leetcode.com/contest/weekly-contest-235/problems/finding-the-users-active-minutes/
class Solution:
    def findingUsersActiveMinutes(
            self, logs: list[list[int]],
            k: int) -> list[int]:
        d = {}
        for a, b in logs:
            d.setdefault(a, set()).add(b)
        _list = [0 for i in range(k)]
        for v in d.values():
            _list[len(v) - 1] += 1
        return _list
