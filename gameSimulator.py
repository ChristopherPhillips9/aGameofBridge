#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

# This file is to play the game from what bridgeGenerator.py generates. It will return the number of players that make
# it across. If there are 20 players, it might return anywhere from 20-0 people depending on how many make it

# pawn = the person who will be trying to make it across

from random import randint
from bridgeGenerator import bridgeGenerator
from pawnGuess import pawnGuess


def playingBoard(players, bridge):
    # Define the number of players remaining
    remainingPlayers = players

    # Iterates through all the segments of the bridge. currentSegment is incremented when a correct tile guess is made.
    currentSegment = 0

    while currentSegment in range(len(bridge)):

        # Returns a single integer as the guess from pawnGuess
        tileGuess = pawnGuess(bridge[currentSegment])

        # Test to see how the game is playing and making sure its working correctly
        # print("Remaining Players:", str(remainingPlayers) + ".", "bridge:", str(bridge))

        # If the guess is incorrect:
        # The remainingPlayers count decreases and currentSegment is not increased
        # The tile is replaced with X. There will be no consequences if tileGuess chooses this tile.
        if bridge[currentSegment][tileGuess] == 1:
            remainingPlayers = remainingPlayers - 1
            bridge[currentSegment][tileGuess] = "X"
            if remainingPlayers == 0:
                return 0
        # If the guess is correct:
        # The currentSegment increases. The tile is replaced with C. This helps visualize the game
        elif bridge[currentSegment][tileGuess] == 0:
            bridge[currentSegment][tileGuess] = "C"
            currentSegment = currentSegment + 1
            if currentSegment >= len(bridge):
                return remainingPlayers


def simulateGame(players, segments, tiles, incorrect):
    # Generates a bridge for the game to be played on
    bridge = bridgeGenerator(segments, tiles, incorrect)

    # Play the game
    results = playingBoard(players, bridge)

    return results

# Example of how to use this code:
# playGame(Number of players, number of segments, number of tiles per segment, number of incorrect tiles per segment)
