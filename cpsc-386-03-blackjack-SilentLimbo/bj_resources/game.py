

from bj_resources import card
from time import sleep

class BlackJackGame:
    def __init__(self):
        self._deck = Deck(1, 10)
        self._game_is_not_over = True
        
    def run(self):
        while self._game_is_not_over:
            print('Top of game loop')
            