class TickTackGame:
    large = 3
    width = 3
    board: list[list]

    def __init__(self, init_string=None):
        self.board = [[None for _ in range(self.width)] for _ in range(self.large)]
        if init_string:
            index = 0
            for i in range(self.large):
                for j in range(self.width):
                    if init_string[index] == "X":
                        self.board[i][j] = True
                    elif init_string[index] == "O":
                        self.board[i][j] = False
                    else:
                        self.board[i][j] = None
                    index += 1
