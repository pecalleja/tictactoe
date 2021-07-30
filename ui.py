class ConsoleRender:
    def __init__(self, game: list[list[bool]]):
        self.game = game

    def render(self):
        print("---------")
        for row in self.game:
            total = len(row)
            the_row = ""
            for index, col in enumerate(row):
                if col is True:
                    element = "X"
                elif col is False:
                    element = "O"
                else:
                    element = "_"
                if index != total-1:
                    element += " "
                the_row += element
            print("| " + the_row + " |")
        print("---------")
