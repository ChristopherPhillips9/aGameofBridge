#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from gameResults import averageSuccessRate

# Cool title image. Nothing else.
print("\n....███........██████......███....██.....██.████████.....███████..████████....████████..████████..████.████████...██████...████████.")
print("...██.██......██....██....██.██...███...███.██..........██.....██.██..........██.....██.██.....██..██..██.....██.██....██..██.......")
print("..██...██.....██.........██...██..████.████.██..........██.....██.██..........██.....██.██.....██..██..██.....██.██........██.......")
print(".██.....██....██...████.██.....██.██.███.██.██████......██.....██.██████......████████..████████...██..██.....██.██...████.██████...")
print(".█████████....██....██..█████████.██.....██.██..........██.....██.██..........██.....██.██...██....██..██.....██.██....██..██.......")
print(".██.....██....██....██..██.....██.██.....██.██..........██.....██.██..........██.....██.██....██...██..██.....██.██....██..██.......")
print(".██.....██.....██████...██.....██.██.....██.████████.....███████..██..........████████..██.....██.████.████████...██████...████████.")
print("............................................................................................................By Christopher Phillips.\n")


# This is the menu for the program
def programLoop():
    # The program loops until quit is called
    while True:
        print(" 1) Simulate the average number of survivors")
        print(" 2) Play the game yourself")
        print(" 3) Quit")

        print("Please select an option:")
        menuSelection = input("choose (1, 2, 3): ")

        # If the user wants to simulate the game
        if menuSelection == str(1):

            # user inputs
            print("Enter the number of simulations. (Recommended amount is 1000).")
            simulations = int(input("simulations: "))
            print("Enter the number of players.")
            players = int(input("players: "))
            print("Enter the length of the bridge in segments (must be >= 1).")
            segments = int(input("Segments: "))
            print("Enter the number of tiles per segment (must be >= 2).")
            tiles = int(input("Tiles: "))
            print("Enter the number of unsafe panes per segment (must be < number of tiles).")
            unsafe = int(input("Unsafe: "))

            # Checker to see if the inputs are valid. Function returns a string if invalid.
            selectionChecker = menuSelectionChecker(simulations, players, segments, tiles, unsafe)

            if selectionChecker == True:
                print("Given:", players, "players,", segments, "segments,", tiles, "tiles,",
                      "and", unsafe, "unsafe tiles:")
                print("The average number of survivors is: ",
                      averageSuccessRate(simulations, players, segments, tiles, unsafe))
                # This is a hacky way to get the menu to pause. It needs a variable otherwise it will require 2 "enters"
                ignoreThisVariable = input("Press ENTER to continue...")
            else:
                print(selectionChecker)

        # If the user wants to play the game
        elif menuSelection == str(2):

            # user inputs
            print("Enter the number of players.")
            players = int(input("players: "))
            print("Enter the length of the bridge in segments (must be >= 1).")
            segments = int(input("Segments: "))
            print("Enter the number of tiles per segment (must be >= 2).")
            tiles = int(input("Tiles: "))
            print("Enter the number of unsafe panes per segment (must be < number of tiles).")
            unsafe = int(input("Unsafe: "))

            # This allows the number of simulations to be fine and dandy
            simulations = 1

            # Checker to see if the inputs are valid. Function returns a string if invalid.
            selectionChecker = menuSelectionChecker(simulations, players, segments, tiles, unsafe)

            if selectionChecker == True:
                pass
            else:
                print(selectionChecker)

        # If the user wants to quit the application
        elif menuSelection == str(3):
            quit(0)

        # If the user didn't enter the correct thing
        else:
            print("\n", menuSelection, "is not a valid option. Please type 1, 2, or 3.\n")


def menuSelectionChecker(simulations, players, segments, tiles, unsafe):
    # This checks to see if all the user inputs are correct

    # This is an error message string that will be generated if the user enters incorrect variables
    errorMessage = "Error: "

    # Each true if statement will add onto the error message
    if int(simulations) == 0:
        errorMessage = errorMessage + "You must have more than 0 simulations. "
    if int(players) == 0:
        errorMessage = errorMessage + "You must have more than 0 players. "
    if int(segments) == 0:
        errorMessage = errorMessage + "You must have more than 0 segments. "
    if int(tiles) < 2:
        errorMessage = errorMessage + "There must be at least 2 panes per segment. "
    if int(unsafe) > int(tiles):
        errorMessage = errorMessage + "There cannot be more unsafe panes than there are panes. "

    # This sees if the errorMessage was populated with more than just "Error:" if it was then it returns the message
    # If it is not populated beyond "Error:" than it returns True
    if errorMessage == "Error: ":
        return True
    else:
        return errorMessage


programLoop()
