#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from bridgeGenerator import bridgeGenerator
from gameRenderer import bridgeObfuscator, bridgeGUI, endGameScreen
from gameResults import averageSuccessRate

# This allows the user to play through the game.
# The user starts with however many specified players that they have and if the player count reaches 0, they lose.
# If the player plays multiple times than the average amount of survivors will be printed out


def oddsOfTheCurrentPlayerSurviving(totalSegments, currentPanes, unsafe, currentUnsafe, currentSegment, totalPanes):
    # Calculates the odds of the current player surviving the current segment.
    odds = [((currentPanes - currentUnsafe) / currentPanes)]

    # Calculates the rest of the chances of surviving the panes and adds them up.
    for i in range(totalSegments - currentSegment - 1):
        odds.append((totalPanes - unsafe) / totalPanes)
    print(odds)

    # Multiplies all the odds together
    newOdds = 1

    for i in range(len(odds)):
        newOdds = newOdds * odds[i]

    # Multiplies newOdds by 100 to return a percentage
    newOdds = (newOdds * 100)
    return newOdds


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

    # Used for the end game screen to display original player amount
    originalPlayers = players

    # Generate the bridge for the game
    bridge = bridgeGenerator(segments, tiles, unsafe)

    # Generate the bridge that will be displayed to the player
    obfuscatedBridge = bridgeObfuscator(bridge)

    # start the game at segment 0
    currentSegment = 0

    # Average number of players to survive the specified bridge
    odds = averageSuccessRate(1000, players, segments, tiles, unsafe)

    # Used for odds of the current player winning
    remainingSafePanes = tiles
    remainingUnsafePanes = unsafe

    # Game loop. currentSegment will advance once the player count increases
    while currentSegment < len(bridge):

        # Calculate the odds of the current player winning
        oddsOf1PlayerSurvival = oddsOfTheCurrentPlayerSurviving(
            segments,
            remainingSafePanes,
            unsafe,
            remainingUnsafePanes,
            currentSegment,
            tiles
        )

        # Save the guess from the GUI and reprint the game window
        tileGuess = bridgeGUI(obfuscatedBridge, players, odds, oddsOf1PlayerSurvival)

        # Checker to see if tileGuess is wrong
        tileGuess = int(guessChecker(tileGuess, int(len(bridge[0])), obfuscatedBridge[currentSegment]))

        # This code looks similar to the pawnGuess code, but it is slightly different
        # Logic for if the player guesses incorrectly
        if bridge[currentSegment][tileGuess] == 1:
            players = players - 1

            # Decreases the count of the remaining safe and unsafe tiles by 1
            remainingSafePanes = remainingSafePanes - 1
            remainingUnsafePanes = remainingUnsafePanes - 1

            obfuscatedBridge[currentSegment][tileGuess] = "X"
            if players == 0:
                outcome = "lose"
                endGameScreen(outcome, odds, players, originalPlayers, segments, tiles, unsafe)
                return
        # If the guess is correct:
        # The currentSegment increases. The tile is replaced with C. This helps visualize the game
        elif bridge[currentSegment][tileGuess] == 0:
            obfuscatedBridge[currentSegment][tileGuess] = "C"
            currentSegment = currentSegment + 1

            # Resets the count for unsafe and safe panes because the game moves to a new segment
            remainingSafePanes = tiles
            remainingUnsafePanes = unsafe

            if currentSegment >= len(bridge):
                outcome = "win"
                endGameScreen(outcome, odds, players, originalPlayers, segments, tiles, unsafe)
                return
