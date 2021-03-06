class TickTackGame:
    large = 3
    width = 3
    board: list[list]
    transposed_board: list[list]
    missing = 0
    x_count = 0
    o_count = 0
    winners = {}

    def __init__(self, init_string=None):
        self.board = [[None] * self.width for _ in range(self.large)]
        self.transposed_board = [[None] * self.width for _ in range(self.large)]
        self.diagonals_up = [None] * self.width
        self.diagonals_down = [None] * self.large

        if init_string:
            index = 0
            for i in range(self.large):
                for j in range(self.width):
                    self.board[i][j] = init_string[index]
                    self.transposed_board[j][i] = init_string[index]
                    if init_string[index] == "X":
                        self.x_count += 1
                    elif init_string[index] == "O":
                        self.o_count += 1
                    else:
                        self.missing += 1
                    if i == j:
                        self.diagonals_down[i] = self.board[i][j]
                    if i + j == self.large - 1:
                        self.diagonals_up[i] = self.board[i][j]
                    index += 1

        self.winners["X"] = self.check_player_win("X")
        self.winners["O"] = self.check_player_win("X")

    def check_player_win(self, player) -> bool:
        if player == "X":
            match = ["X", "X", "X"]
        else:
            match = ["O", "O", "O"]
        rows = match in self.board
        columns = match in self.transposed_board
        diagonal = match in [self.diagonals_up, self.diagonals_down]
        return any([rows, columns, diagonal])

    def make_a_move(self, player, row, col):
        if self.board[row][col] not in ["X", "O"]:
            self.board[row][col] = player
            self.transposed_board[col][row] = player
            self.missing -= 1
            if col == row:
                self.diagonals_down[col] = self.board[row][col]
            if col + row == self.large - 1:
                self.diagonals_up[row] = self.board[row][col]
        else:
            raise ValueError("This cell is occupied!")

        self.winners[player] = self.check_player_win(player)

    def check_game_status(self):
        if self.winners["X"] and not self.winners["O"]:
            return "X wins"
        elif self.winners["O"] and not self.winners["X"]:
            return "O wins"
        elif self.winners["X"] is False and self.winners["O"] is False and self.missing == 0:
            return "Draw"
        else:
            return None
