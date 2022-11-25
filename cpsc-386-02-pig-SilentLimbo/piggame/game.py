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


"""Game class for my game"""

from .dice import Die
from .player import Player, ComputerPlayer


class PigGame:
    """class for the game"""

    def __init__(self):
        """makes max score and player list"""
        self._players = []
        self._max_score = 30

    def opponent_score(self):
        """returns op score to bot, but as of right now it does nothing..."""
        # for player in self._players:
        #   if _me != player:
        #       return player.score

    def run(self):
        """runs the game"""
        _d = Die()
        num_players = int(input("How many players? [1-4] "))
        for _ in range(num_players):
            name = input("What is your name? ")
            order = _d.roll()
            print("You rolled {}.".format(order))
            self._players.append(Player(name, order))
        if num_players == 1:
            order = _d.roll()
            print("The Comp rolled {}.".format(order))
            self._players.append(ComputerPlayer(order, self))
            num_players = 2

        self._players.sort(key=lambda p: p.order, reverse=True)
        print("The player order is as follows: {}\n".format(self._players))
        current_player_index = 0
        current_score = 0
        _cp = self._players[current_player_index]

        while _cp.score < self._max_score:
            _cp = self._players[current_player_index]
            if _cp.are_you_human():
                print("{}'s turn: \n".format(_cp.name))
                rolling = input(
                    "{}'s current stats: (total: {}, current: {})\nRoll? (y or n) >".format(
                        _cp, _cp.score, current_score
                    )
                ).lower()
                if rolling == "y":
                    rolled = _d.roll()
                    print("You rolled {}".format(rolled))
                    if rolled == 1:
                        print(
                            "\nBig oof, you lost your current score of {}, total: {}\n".format(
                                current_score, _cp.score
                            )
                        )
                        current_score = 0
                        current_player_index = (
                            current_player_index + 1
                        ) % num_players
                    else:
                        current_score += rolled
                else:
                    print("{} wants to end their turn.".format(_cp))
                    _cp.score += current_score
                    if _cp.score >= self._max_score:
                        break
                    print(
                        "{} is currently holding a score of {}\n".format(
                            _cp, _cp.score
                        )
                    )
                    print("*" * 80)
                    current_score = 0
                    current_player_index = (
                        current_player_index + 1
                    ) % num_players
            else:
                print("{} is up\n".format(_cp.name))
                current_score = _cp.does_roll()
                print("{} has end their turn.\n".format(_cp))
                _cp.score += current_score
                if _cp.score >= self._max_score:
                    break
                print(
                    "{} is currently holding a score of {}\n".format(
                        _cp, _cp.score
                    )
                )
                current_score = 0
                current_player_index = (current_player_index + 1) % num_players

        print("\nPlayer {} wins with a score of {}".format(_cp, _cp.score))
