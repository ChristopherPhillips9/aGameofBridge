#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from bridgeGenerator import bridgeGenerator
from bridgeRenderer import bridgeObfuscator, bridgeGUI
from gameSimulator import simulateGame

# This allows the user to play through the game.
# The user starts with however many specified players that they have and if the player count reaches 0, they lose.
# If the player plays multiple times than the average amount of survivors will be printed out


def guessChecker(guess, length, obfuscated):
    # Check to see if the guess is valid against the length of the array
    # Endless loop to return valid input
    while True:
        # Check to make sure input is not blank
        if str(guess) == "":
            print("Error, that input is blank!")
            guess = input("Input: ")
        else:
            # Check to see if the number is in range
            if -1 < int(guess) < (int(length)):
                # Check to see if the number is marked X.
                if obfuscated[int(guess)] != "X":
                    return int(guess)
                else:
                    print("Error, that tile is already broken")
                    guess = input("Input: ")
            else:
                print("Error, the input is out of range")
                guess = input("Input: ")


def playGame(players, segments, tiles, unsafe):
    # This creates the variables for the game and outputs them here

    # Generate the bridge for the game
    bridge = bridgeGenerator(segments, tiles, unsafe)

    # Generate the bridge that will be displayed to the player
    obfuscatedBridge = bridgeObfuscator(bridge)

    # start the game at segment 0
    currentSegment = 0

    # Average number of players to survive the specified bridge
    odds = simulateGame(players, segments, tiles, unsafe)

    # Game loop. currentSegment will advance once the player count increases
    while currentSegment < len(bridge):

        # Save the guess from the GUI and reprint the game window
        tileGuess = bridgeGUI(obfuscatedBridge, players, odds)

        # Checker to see if tileGuess is wrong
        tileGuess = int(guessChecker(tileGuess, int(len(bridge[0])), obfuscatedBridge[currentSegment]))

        # This code looks similar to the pawnGuess code, but it is slightly different
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
