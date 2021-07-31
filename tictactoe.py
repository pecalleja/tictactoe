import ui
import game


init_string = input("Enter cells:")

the_game = game.TickTackGame(init_string)
ui.ConsoleRender(the_game.board).render()
if the_game.x_win and not the_game.o_win:
    print("X wins")
elif the_game.o_win and not the_game.x_win:
    print("O wins")
elif the_game.o_win is False and the_game.x_win is False and the_game.missing == 0:
    print("Draw")
elif (
        (the_game.o_win is True and the_game.o_win is True) or
        (abs(the_game.o_count - the_game.x_count) > 1)
):
    print("Impossible")
else:
    print("Game not finished")
