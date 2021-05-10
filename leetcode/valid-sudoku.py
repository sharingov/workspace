# https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        _list = [set() for _ in range(9)]
        ver = [set() for _ in range(9)]
        for i in range(9):
            hor = set()
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    source = _list[(i // 3) * 3 + j // 3]
                    if val not in source:
                        source.add(val)
                    else:
                        return False
                    if val not in hor:
                        hor.add(val)
                    else:
                        return False
                    if val not in ver[j]:
                        ver[j].add(val)
                    else:
                        return False
        return True
