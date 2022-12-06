#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

# This file is to play the game from what bridgeGenerator.py generates. It will return the number of players that make
# it across. If there are 20 players, it might return anywhere from 20-0 people depending on how many make it

# pawn = the person who will be trying to make it across

from bridgeGenerator import bridgeGenerator


def pawnGuess():
    pass


def playingBoard(players, bridge):
    # Define the number of players remaining
    remainingPlayers = players

    print(bridge)
    pass


def playGame(players, segments, tiles, incorrect):
    # Generates a bridge for the game to be played on
    bridge = bridgeGenerator(segments, tiles, incorrect)

    # Play the game
    playingBoard(players, bridge)

    pass


# Example of how to use this code:
# playGame(Number of players, number of segments, number of tiles per segment, number of incorrect tiles per segment)
playGame(20, 18, 2, 1)