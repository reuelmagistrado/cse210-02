import random

__assignment__ = "Week 2: Hilo Game"
__course__ = "CSE 210: Programming with Classes"
__author__ = "Reuel Magistrado"
__version__ = "1.0.0"
__maintainer__ = "Reuel Magistrado"
__email__ = "mag21010@byui.edu"


class Dealer:
    """A person who handles, and draws card.

    The responsibility of Dealer is to keep track of the cards, ask the player to guess, and compare if the first drawn card is higher or lower to the second drawn card.

    Attributes:
        cards (list): The index of cards in the art.py file.
    """


# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Dealer with a cards attribute.

        Args:
            self (Die): An instance of Die.
        """
        self.cards = random.sample(range(0, 13), 2)

    def ask_player(self):
        """Returns a question to the player.

        Args:
            self (Die): An instance of Die.
        """

        return input("Higher or lower? [h/l] ")

    def is_player_card_higher(self):
        """Returns true if the first card is lower than the second card, otherwise false.

        Args:
            self (Die): An instance of Die.
        """

        return self.cards[0] < self.cards[1]
