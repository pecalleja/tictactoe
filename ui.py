class ConsoleRender:
    def __init__(self, game: list[list[bool]]):
        self.game = game

    def render(self):
        for row in self.game:
            total = len(row)
            the_row = ""
            for index, col in enumerate(row):
                element = "X" if col else "O"
                if index != total-1:
                    element += " "
                the_row += element
            print(the_row)
