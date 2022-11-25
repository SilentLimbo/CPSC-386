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


"""Dice class for our game."""

from random import randrange


class Die:
    """dice class"""

    def __init__(self):
        """initializing dice as an object?"""
        return

    @property
    def random(self):
        """returns random number between 1-10"""
        return randrange(1, 11)

    @property
    def roll(self):
        """defining what roll does"""
        return randrange(1, 7)
