from colorama import Fore as color, init

init(autoreset=True)

def game_continue(message: str = 'Press ENTER to Continue...'):
    input(color.GREEN + message.upper())

def game_over(message: str = color.RED + 'Game Over'):
    print(message.upper())
