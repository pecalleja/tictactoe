import ui
import game


init_string = input("Enter cells:")

ui.ConsoleRender(game.TickTackGame(init_string).board).render()
