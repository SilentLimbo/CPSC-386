

from card import Deck

class Player:
    pass

class Dealer:
    def __init__(self, n_decks = 1, cut_card_min = 51, \
        cut_card_max = 51):
        self._deck = Deck(cut_card_min, cut_card_max)
        for _ in range(n_decks - 1):
            self._deck.merge(Deck(cut_card_min, cut_card_max))
        
    def deal_to(self, player):
        pass
    def check_shoe(self):
        pass