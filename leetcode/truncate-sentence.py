# https://leetcode.com/contest/weekly-contest-235/problems/truncate-sentence/
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split(' ', k)[:k])
