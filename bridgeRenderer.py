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
    print("\nplayers remaining:", players)
    print("\nChances of the current player surviving:", )
    print("\nAverage survival amount for this bridge:", odds)

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

    print("\n Which tile will you move to next? choose a tile from 0 to "+ str(len(bridge[i])-1))
    return input("Input: ")
