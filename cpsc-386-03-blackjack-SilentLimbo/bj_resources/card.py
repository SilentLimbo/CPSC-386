
from collections import namedtuple
from random import shuffle, randrange
from math import floor

Card = namedtuple('Card', ['rank', 'suit'])

def stringify_card(c):
    return '{} of {}'.format(c.rank, c.suit)

Card.__str__ = stringify_card

class Deck:
    ranks = ['Ace'] + [str(x) for x in range(2, 11)] + \
        'Jack Queen King'.split()
    suits = 'Clubs Hearts Spades Diamonds'.split()
    
    def __init__(self, \
        cut_card_position_min = 0, cut_card_position_max = 0):
        if cut_card_position_max == 0 and \
            cut_card_position_min == 0:
                self._cut_card_position = 0
        else:
            self._cut_card_position = randrange(\
                cut_card_position_min,\
                cut_card_position_max)
##        print('cut card is at ', self._cut_card_position)
        self._cards = [Card(rank, suit) \
            for suit in self.suits \
            for rank in self.ranks]
        
    @property
    def needs_shuffle(self):
        return len(self._cards) <= self._cut_card_position

    def __getitem__(self, position):
        return self._cards[position]
    
    def __len__(self):
        return len(self._cards)
    
    def shuffle(self, n=1):
        for _ in range(n):
            shuffle(self._cards)
            
    def cut(self):
        p = floor(len(self._cards) * .2)
        half = (len(self._cards) // 2) + \
        randrange(-p, p)
        tophalf = self._cards[:half]
        bottomhalf = self._cards[half:]
        self._cards = bottomhalf + tophalf
        
    def deal(self, n=1):
        return [self._cards.pop(0) for _ in range(n)]

    def merge(self, other_deck):
        self._cards = self._cards + other_deck._cards

    def __str__(self):
        return '\n'.join(map(str, self._cards))

def demo():
    d = Deck()
    print(d)
    d.shuffle(10)
    d.cut()
    print('\nShuffled')
    print(d)


if __name__ == '__main__':
    demo()
