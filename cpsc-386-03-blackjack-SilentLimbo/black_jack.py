#!/usr/bin/env python3
# Mina Ghaly
# CPSC 386-04
# 2022-04-04
# mghaly@csu.fullerton.edu
# @SilentLimbo
#
# Lab 00-02
#
# This is BlackJack game
#


"""Game run file"""


from bj_resources import game

if __name__ == "__main__":
    GAME = game.BlackJackGame()
    GAME.run()
