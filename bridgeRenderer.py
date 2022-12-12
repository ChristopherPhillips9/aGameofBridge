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
            displayBridge[i][j] = "?"

    return displayBridge


def bridgeWindow(bridge):
    pass


