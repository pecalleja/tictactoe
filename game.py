class TickTackGame:
    large = 3
    width = 3
    board: list[list]
    transposed_board: list[list]
    missing = 0
    x_count = 0
    o_count = 0
    x_win = None
    o_win = None

    def __init__(self, init_string=None):
        self.board = [[None] * self.width for _ in range(self.large)]
        self.transposed_board = [[None] * self.width for _ in range(self.large)]
        self.diagonals_up = [None] * self.width
        self.diagonals_down = [None] * self.large

        if init_string:
            index = 0
            for i in range(self.large):
                for j in range(self.width):
                    if init_string[index] == "X":
                        self.board[i][j] = True
                        self.transposed_board[j][i] = True
                        self.x_count += 1
                    elif init_string[index] == "O":
                        self.board[i][j] = False
                        self.transposed_board[j][i] = False
                        self.o_count += 1
                    else:
                        self.board[i][j] = None
                        self.transposed_board[j][i] = None
                        self.missing += 1
                    if i == j:
                        self.diagonals_down[i] = self.board[i][j]
                    if i + j == self.large - 1:
                        self.diagonals_up[i] = self.board[i][j]
                    index += 1

        self.x_win = self.check_player_win("X")
        self.o_win = self.check_player_win("O")

    def check_player_win(self, player) -> bool:
        if player == "X":
            match = [True, True, True]
        else:
            match = [False, False, False]
        rows = match in self.board
        columns = match in self.transposed_board
        diagonal = match in [self.diagonals_up, self.diagonals_down]
        return any([rows, columns, diagonal])
