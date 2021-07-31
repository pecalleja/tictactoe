class ConsoleRender:
    def __init__(self, board: list[list[bool]]):
        self.board = board

    def render(self):
        print("---------")
        for row in self.board:
            total = len(row)
            the_row = ""
            for index, col in enumerate(row):
                element = col
                if index != total-1:
                    element += " "
                the_row += element
            print("| " + the_row + " |")
        print("---------")
