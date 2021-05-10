# https://leetcode.com/problems/sudoku-solver/
import numpy as np


class Solution:
    stop = False

    def solve(self, board, a, b):
        def decide():
            if a == 8 and b == 8:
                Solution.stop = True
            elif b != 8:
                self.solve(board, a, b + 1)
            else:
                self.solve(board, a + 1, 0)
        if board[a, b] > 0:
            decide()
        else:
            for i in range(1, 10):
                board[a, b] = i
                hor = np.count_nonzero(board[a] == i) == 1
                ver = np.count_nonzero(board[:, b] == i) == 1
                box = np.count_nonzero(
                    board[(a // 3) * 3:(a // 3) * 3 + 3,
                          (b // 3) * 3:(b // 3) * 3 + 3] == i) == 1
                if hor and ver and box:
                    decide()
                if Solution.stop:
                    return
                board[a, b] = 0

    def solveSudoku(self, board: list[list[str]]) -> None:
        def convert(s):
            return 0 if s == '.' else int(s)
        a = np.array(list(list(map(convert, board[i])) for i in range(9)))
        self.solve(a, 0, 0)
        board[:] = a.astype(str).tolist()
        Solution.stop = False
