#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from random import randint


def guessReconstructor(list1, list2):
    # Reconstructs the guess from pawnGuess() back together to produce a meaningful output.
    currentWithoutStr = list1
    currentWithoutInt = list2

    # This value will increase every time an element in currentWithoutStr is increased.
    currentArrayValue = 0

    for i in range(len(currentWithoutInt)):

        # Every element that is not "X" in currentWithoutInt will be changed to the value from currentWithoutInt
        if currentWithoutInt[i] != "X":
            currentWithoutInt[i] = currentWithoutStr[currentArrayValue]
            currentArrayValue = currentArrayValue + 1

            if currentWithoutInt[i] == "G":
                # if the value of G was found and its position is now known, return the value
                return i


def pawnGuess(current):
    # currentWithoutInt is the list "current" without any integers
    # currentWithoutInt also holds the length of the original "current" input
    currentWithoutInt = []

    # currentWithoutStr is the list "current" without any strings
    currentWithoutStr = []

    # Loop to make currentWithoutInt all 0's for the length of current.
    for i in range(len(current)):
        currentWithoutInt.append(0)

    # Loop to apply all X's to currentWithoutInt from their position in current.
    for i in range(len(current)):

        if isinstance(current[i], str):
            currentWithoutInt[i] = "X"

    # Add all integer values from current into currentWithoutInt
    for i in range(len(current)):
        if isinstance(current[i], int):
            currentWithoutStr.append(current[i])

    # Make the guess
    # Choose a random integer between 0 and the length of currentWithoutStr.
    randomArraySelection = randint(0, len(currentWithoutStr) - 1)
    # Take that number and apply it to the position in currentWithoutStr. "G" stands for guess
    currentWithoutStr[randomArraySelection] = "G"

    # Tie it all together with guessReconstructor()
    currentWithoutInt = guessReconstructor(currentWithoutStr, currentWithoutInt)

    return currentWithoutInt


# For testing purposes:

# print("returns 1:")
# for j in range(10):
#     print(pawnGuess(["X", 0]))

# print("returns 0:")
# for j in range(10):
#     print(pawnGuess([0, "X"]))
#
# print("returns 1, 3, or 4:")
# for j in range(10):
#     print(pawnGuess(["X", 0, "X", 1, 0, "X"]))
