#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from random import randint


# This file is used for generating a bridge for use in the game

def bridgeGenerator(s, k, c):
    # s = total number of segments
    # k = total number of panes
    # c = number of correct/safe panes

    bridgeRow = [] * s

    # This creates a 2d matrix. i is iterating through the num of segments while j iterates through the num of panes
    for i in range(s):

        bridgeColumn = [0] * k

        # ii is used because k is taken (i -> j -> k). ii resets here
        ii = 0
        for j in range(k):

            while ii < c:
                # randint from random library. Finds a random integer from 0 to c, the length of the array k.
                # placeInt = the randomly chosen value that will modify the array
                placeInt = randint(0, c)

                if bridgeColumn[placeInt] == 0:
                    bridgeColumn[placeInt] = 1
                    ii = ii + 1

        bridgeRow.append(bridgeColumn)

    return bridgeRow

# Examples of use:
# bridge for Problem 1: print(bridgeGenerator(18, 2, 1))
