# Mina Ghaly
# CPSC 386-04
# 2022-03-07
# mghaly@csu.fullerton.edu
# @SilentLimbo
#
# Lab 00-01
#
# This is pig dice game
#


"""Player class for my game"""
import time
from piggame.dice import Die


class Player:
    """player class"""

    def __init__(self, name, order):
        """init declare for player"""
        self._name = name
        self._score = 0
        self._order = order

    @property
    def name(self):
        """returns name"""
        return self._name

    @property
    def score(self):
        """returns score"""
        return self._score

    @property
    def order(self):
        """returns order"""
        return self._order

    @score.setter
    def score(self, new_score):
        """sets a new score"""
        self._score = new_score

    def __str__(self):
        """str name"""
        return self._name

    def __repr__(self):
        """format player list"""
        return 'Player("{}", {})'.format(self._name, self._order)


class ComputerPlayer(Player):
    """computer class"""

    def __init__(self, order, game):
        """defines computer player"""
        super().__init__("Kermit_bot", order)
        self._game = game

    def does_roll(self):
        """computer ai for rolling"""
        score = self._score
        _d = Die()
        c_score = 0

        while True:
            if score < 25:
                if c_score < 10:
                    rolled = _d.roll()
                    print("{} rolled {}".format(self._name, rolled))
                    time.sleep(2)
                    if rolled == 1:
                        c_score = 0
                        return c_score
                    c_score += rolled
                else:
                    return c_score
            if score >= 25:
                if c_score < 5:
                    rolled = _d.roll()
                    print("{} rolled {}".format(self._name, rolled))
                    time.sleep(2)
                    if rolled == 1:
                        c_score = 0
                        return c_score
                    c_score += rolled
                else:
                    return c_score
