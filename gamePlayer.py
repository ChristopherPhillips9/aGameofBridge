#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from bridgeGenerator import bridgeGenerator
from bridgeRenderer import bridgeObfuscator, bridgeGUI

# This allows the user to play through the game.
# The user starts with however many specified players that they have and if the player count reaches 0, they lose.
# If the player plays multiple times than the average amount of survivors will be printed out


def guessChecker():
    pass


def playGame(players, segments, tiles, unsafe):
    # This creates the variables for the game and outputs them here

    # Generate the bridge for the game
    bridge = bridgeGenerator(segments, tiles, unsafe)

    # Generate the bridge that will be displayed to the player
    obfuscatedBridge = bridgeObfuscator(bridge)

    # start the game at segment 0
    currentSegment = 0

    # TODO: add simulation results for expected player survival rate
    odds = "undefined"

    # Game loop. currentSegment will advance once the player count increases
    while currentSegment < len(bridge):

        # Save the guess from the GUI and reprint the game window
        tileGuess = bridgeGUI(obfuscatedBridge, players, odds)

        # Convert tileGuess into an int
        tileGuess = int(tileGuess)

        # This code looks similar to the code inside of pawnGuess but it is slightly different
        # Logic for if the player guesses incorrectly
        if bridge[currentSegment][tileGuess] == 1:
            players = players - 1
            obfuscatedBridge[currentSegment][tileGuess] = "X"
            if players == 0:
                return 0
        # If the guess is correct:
        # The currentSegment increases. The tile is replaced with C. This helps visualize the game
        elif bridge[currentSegment][tileGuess] == 0:
            obfuscatedBridge[currentSegment][tileGuess] = "C"
            currentSegment = currentSegment + 1
            if currentSegment >= len(bridge):
                print("Game won!")
                return players


print(playGame(20, 18, 2, 1))
