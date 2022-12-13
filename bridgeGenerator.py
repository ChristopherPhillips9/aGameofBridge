#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from random import randint

# This file is used for generating a bridge for use in the game or simulation


def bridgeGenerator(s, k, c):
    # s = total number of segments
    # k = total number of panes
    # c = number of unsafe panes

    bridgeRow = []

    # This creates a 2d matrix. var i is iterating through the num of segments while j iterates through the num of panes
    for i in range(s):

        # Creates multiple segments of the bridge of all 0's with k number of elements
        bridgeColumn = [0] * k

        # ii is named ii because k is taken (i -> j -> k). ii resets here
        # ii increases when a random integer in the column is changed from 0 to 1
        ii = 0
        for j in range(k):

            # This loop runs until enough random integers for the list are chosen
            while ii < c:
                # randint from random library. Finds a random integer from 0 to c, the length of the array k
                # placeInt = the randomly chosen value that will modify the list
                placeInt = randint(0, c)

                # If the list element placeInt found is equal to 0, then change it to 1
                if bridgeColumn[placeInt] == 0:
                    bridgeColumn[placeInt] = 1
                    ii = ii + 1

        # Once the bridgeColumn has the defined numbers it needs, add it as a segment to the bridge
        bridgeRow.append(bridgeColumn)

    return bridgeRow

# Examples of use:
# bridge for problem 1: print(bridgeGenerator(18, 2, 1))
