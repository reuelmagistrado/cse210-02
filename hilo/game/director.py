from os import system
from game.dealer import Dealer
from game.art import game_over, logo, cards

__assignment__ = "Week 2: Hilo Game"
__course__ = "CSE 210: Programming with Classes"
__author__ = "Reuel Magistrado"
__version__ = "1.0.0"
__maintainer__ = "Reuel Magistrado"
__email__ = "mag21010@byui.edu"


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dealer (Dealer): An instance of Dealer class.
        is_playing (boolean): Whether or not the game is being played.
        points (int): The initial score of a player.
        total_score (int): The score for the entire game.
        points_added (int): Points added to the total score if guess is correct.
        points_deducted (int): Points deducted to the total score if guess is wrong.
        player_answer (str): Answer of the player if high or low.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.dealer = Dealer()
        self.is_playing = True
        self.points = 300
        self.total_score = self.points
        self.points_added = 100
        self.points_deducted = 75
        self.player_answer = ''

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            print(logo)
            print(f"The card is: {cards[self.dealer.cards[0]]}")
            self.player_answer = self.dealer.ask_player()
            self.do_updates()
            self.do_outputs()

            if self.total_score <= 0:
                print(game_over)
                break

            self.get_inputs()
            self.dealer = Dealer()
            system('cls')

    def get_inputs(self):
        """Ask the user if they want to play again.

        Args:
            self (Director): An instance of Director.
        """
        play_again = input("Play again? [y/n] ")
        self.is_playing = (play_again == "y")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        is_guess_correct = (
            self.player_answer == 'h' and self.dealer.is_player_card_higher()) or (
            self.player_answer == 'l' and not self.dealer.is_player_card_higher())

        if is_guess_correct:
            print('\nCORRECT ✅')
            self.total_score += self.points_added
        else:
            print('\nWRONG ❌')
            self.total_score -= self.points_deducted

    def do_outputs(self):
        """Displays the next card and the score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Next card was: {cards[self.dealer.cards[1]]}")
        print(f"Your score is: {self.total_score}\n")
