from colorama import Fore as color_text_game, init as color_init

color_init(autoreset=True)

red   : str = color_text_game.RED
green : str = color_text_game.GREEN
blue  : str = color_text_game.BLUE
yellow: str = color_text_game.YELLOW

def game_continue(g_continue: str =  'Press ENTER to Continue...'): input(green+g_continue.upper())
def game_over(g_over: str = red+ 'Game Over'): print(red+g_over.upper())