#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

# Takes a bridge generated from bridgeGenerator and makes it display friendly for players.

from copy import deepcopy
from bridgeGenerator import bridgeGenerator


def bridgeObfuscator(bridge):
    # Makes a copy of the bridge that will be filled with '?' instead of anything else so that the player cannot see.

    # deepcopy is used to make an actual copy as opposed to a reference
    displayBridge = deepcopy(bridge)

    # Writes "?" for every element in the original array.
    for i in range(len(displayBridge)):
        for j in range(len(displayBridge[i])):
            displayBridge[i][j] = "█"

    return displayBridge


def bridgeGUI(bridge, players, odds):
    # This is the window that the player sees. It also prints instructions
    # This function returns the choice the player made

    # formatting and header
    print("\n\n")
    print("Key: █ = unknown tile, X = incorrect guess, C = correct guess")
    print("players remaining:", players)
    print("Chances of the current player surviving:", )
    print("Average survival amount for this bridge:", odds)
    print("")

    # print the bridge
    for i in range(len(bridge)):

        # Turn the current section into a string
        displayBridgeSegment = str(bridge[i])

        # Strip away the brackets and commas from displayBridgeSegment
        displayBridgeSegment = displayBridgeSegment.strip("[").strip("]").strip("'").replace(',', '').replace('\'', '')

        # Print out the edited string so that it's good-looking
        # Formatting to add number padding. It works up to 99.
        if i < 10:
            print("segment 0" + str(i) + ": " + displayBridgeSegment)
        elif i < 100:
            print("segment " + str(i) + ": " + displayBridgeSegment)

    print("\nWhich tile will you move to next? choose a tile from 0 to " + str(len(bridge[i]) - 1))
    return input("Input: ")


def endGameScreen(outcome, odds, survivors, players, segments, tiles, unsafe):
    # This screen displays once the player has won the game
    if outcome == "win":
        print("\n..................................................................")
        print("..##############################################################..")
        print("..#............................................................#..")
        print("..#..██..██..██████..██..██....██..██..██..████..██....██..██..#..")
        print("..#..██..██..██..██..██..██....██..██..██...██...████..██..██..#..")
        print("..#...████...██..██..██..██....██..██..██...██...██.██.██..██..#..")
        print("..#....██....██..██..██..██....██..██..██...██...██..████......#..")
        print("..#....██....██████..██████......██..██....████..██....██..██..#..")
        print("..#............................................................#..")
        print("..##############################################################..")
        print("..................................................................\n")
    else:
        print("\nYou lost!\n")

    print("Stats:")
    print("Game parameters:", players, "players,", segments, "segments,", tiles, "tiles, and", unsafe, "unsafe tiles")
    print("Average number of survivors for this bridge:", odds)
    print("Average number of survivors per game:", survivors, "out of", players)
    print("")

    # This is a  way to get the menu to pause. It needs a variable otherwise it will require 2 "enters"
    ignoreThisVariable = input("Press ENTER to continue...")

