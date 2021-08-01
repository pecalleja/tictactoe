import ui
import game


init_string = "_________"
the_game = game.TickTackGame(init_string)
ui.ConsoleRender(the_game.board).render()

players = ["X", "O"]
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

    player = players.pop(0)
    try:
        the_game.make_a_move(player, x - 1, y - 1)
        ui.ConsoleRender(the_game.board).render()
        result = the_game.check_game_status()
        if result is not None:
            print(result)
            break
    except ValueError:
        players.insert(0, player)
        print("This cell is occupied! Choose another one!")
        continue

    players.append(player)
