from colorama import Fore as color_text_game, init as color_init

color_init(autoreset=True)

red   : str = color_text_game.RED
green : str = color_text_game.GREEN
blue  : str = color_text_game.BLUE
yellow: str = color_text_game.YELLOW

def game_continue(g_continue: str = green+ 'Press ENTER to Continue...'.upper()): input(g_continue)
def game_over(g_over: str = red+ 'Game Over'.upper()): print(g_over)