# https://leetcode.com/problems/string-to-integer-atoi/
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.search(r'^[+|-]?\d+', s.lstrip())
        return (match or 0) and max(-2147483648,
                                    min(2147483647, int(match.group())))
