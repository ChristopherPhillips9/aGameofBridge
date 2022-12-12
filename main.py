#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

# from gamePlayer import gamePlayer
# from gameSimulator import

# Cool title image. Nothing else.
print(
    "\n....███........██████......███....██.....██.████████.....███████..████████....████████..████████..████.████████...██████...████████.")
print(
    "...██.██......██....██....██.██...███...███.██..........██.....██.██..........██.....██.██.....██..██..██.....██.██....██..██.......")
print(
    "..██...██.....██.........██...██..████.████.██..........██.....██.██..........██.....██.██.....██..██..██.....██.██........██.......")
print(
    ".██.....██....██...████.██.....██.██.███.██.██████......██.....██.██████......████████..████████...██..██.....██.██...████.██████...")
print(
    ".█████████....██....██..█████████.██.....██.██..........██.....██.██..........██.....██.██...██....██..██.....██.██....██..██.......")
print(
    ".██.....██....██....██..██.....██.██.....██.██..........██.....██.██..........██.....██.██....██...██..██.....██.██....██..██.......")
print(
    ".██.....██.....██████...██.....██.██.....██.████████.....███████..██..........████████..██.....██.████.████████...██████...████████.")
print(
    "............................................................................................................By Christopher Phillips.\n")


# This is the menu for the program
def programLoop():
    # The program loops until quit is called
    while True:
        print(" 1) Simulate the average number of survivors")
        print(" 2) Play the game yourself")
        print(" 3) Quit")

        print("Please select an option:")
        menuSelection = input("choose (1, 2, 3): ")

        if menuSelection == str(1):

            # user inputs
            print("Enter the number of players.")
            players = input("players: ")
            print("Enter the length of the bridge in segments (must be >= 1).")
            segments = input("Segments: ")
            print("Enter the number of tiles per segment (must be >= 2).")
            tiles = input("Tiles: ")
            print("Enter the number of unsafe panes per segment (must be < number of tiles).")
            unsafe = input("Unsafe: ")

            # This is used so that the checker doesn't return false for having no simulations specified
            simulations = 1

            # Checker to see if the inputs are valid
            selectionChecker = menuSelectionChecker(simulations, players, segments, tiles, unsafe)

            if selectionChecker == True:
                print("All settings good!")
            else:
                print(selectionChecker)

        elif menuSelection == str(2):
            pass
        elif menuSelection == str(3):
            quit(0)
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
