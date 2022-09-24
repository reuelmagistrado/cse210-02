from os import system
from game.director import Director

__assignment__ = "Week 2: Hilo Game"
__course__ = "CSE 210: Programming with Classes"
__author__ = "Reuel Magistrado"
__version__ = "1.0.0"
__maintainer__ = "Reuel Magistrado"
__email__ = "mag21010@byui.edu"


def main():
    """Main Program of Hilo Game."""

    # Clear the terminal screen.
    system('cls')
    director = Director()
    director.start_game()
    print('THANKS FOR PLAYING! 🎮👋\n')


# Code to execute if called from command-line.
if __name__ == "__main__":
    main()
