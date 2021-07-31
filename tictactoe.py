import ui
import game


init_string = input("Enter cells:")

the_game = game.TickTackGame(init_string)
ui.ConsoleRender(the_game.board).render()

while True:
    try:
        x, y = input("Enter the coordinates:").split()
        x = int(x)
        y = int(y)
    except ValueError:
        print("You should enter numbers!")
        continue

    if x > len(the_game.board) or y > len(the_game.board[0]):
        print(f"Coordinates should be from 1 to {len(the_game.board)}!")
        continue

    try:
        the_game.make_a_move("X", x - 1, y - 1)
        ui.ConsoleRender(the_game.board).render()
        break
    except ValueError:
        print("This cell is occupied! Choose another one!")
        continue
# if the_game.x_win and not the_game.o_win:
#     print("X wins")
# elif the_game.o_win and not the_game.x_win:
#     print("O wins")
# elif the_game.o_win is False and the_game.x_win is False and the_game.missing == 0:
#     print("Draw")
# elif (
#         (the_game.o_win is True and the_game.o_win is True) or
#         (abs(the_game.o_count - the_game.x_count) > 1)
# ):
#     print("Impossible")
# else:
#     print("Game not finished")
