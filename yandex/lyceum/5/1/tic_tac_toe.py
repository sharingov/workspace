class TicTacToeBoard:
    def new_game(self):
        self.grid = [["-" for _ in range(3)] for _ in range(9)]
        self.grid[0] = [["-" for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.done = False

    def __init__(self):
        self.new_game()

    def get_field(self):
        return self.grid[0]

    def check_field(self):
        full = True
        for cond in self.grid:
            if type(cond[0]) == list:
                for row in cond:
                    for elem in row:
                        if elem == "-":
                            full = False
            elif all(x == cond[0] and x != "-" for x in cond):
                self.done = True
                return cond[0]
        if full:
            self.done = True
            return "D"

    def make_move(self, row, col):
        if self.done:
            return "Игра уже завершена"
        if self.grid[0][row - 1][col - 1] != "-":
            return f"Клетка {row}, {col} уже занята"

        self.grid[0][row - 1][col - 1] = self.turn
        self.grid[row][col - 1] = self.turn
        self.grid[col + 3][row - 1] = self.turn
        if row == col:
            self.grid[7][row - 1] = self.turn
        if row + col == 4:
            self.grid[8][row - 1] = self.turn

        self.turn = "0" if self.turn == "X" else "X"

        res = self.check_field()
        if res == "X":
            return "Победил игрок X"
        elif res == "0":
            return "Победил игрок 0"
        elif res == "D":
            return "Ничья"
        else:
            return "Продолжаем играть"
