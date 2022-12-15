#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

# This file is used to calculate how the average number of survivors increases or decreases

# These bridges are a function that turns x number of players into y number of survivors, so this is the best metric
# ... to use

# We will be using gameResults.averageSuccessRate to calculate the number of survivors

from gameResults import averageSuccessRate

# We will use this to calculate the chances one player has to win from any given point in any given bridge
from oddsOfSurvival import oddsOfTheCurrentPlayerSurviving

# For these questions, our control will be 20 players, 18 segments, 2 tiles per segment, and 1 unsafe tile.


# Question 1: What happens if the number of segments increases?
def increasingNumberOfSegments():
    question1List = []

    for i in range(18, 28):
        question1List.append(averageSuccessRate(simulationTimes, 20, i, 2, 1))

    # This output should be entered into a graph
    print("segments increasing from 18 to 28")
    for i in range(len(question1List)):
        print("x:", i+18, "y:", question1List[i])


# Question 2: What happens if the number of panes increases, but not the number of unsafe panes?
def increasingNumberOfTiles():
    question1List = []

    for i in range(2, 13):
        question1List.append(averageSuccessRate(simulationTimes, 20, 18, i, 1))

    # This output should be entered into a graph
    print("number of total panes increasing from 2 to 12")
    for i in range(len(question1List)):
        print("x:", i + 2, "y:", question1List[i])


# Question 3: What happens if the number of tiles increase AND the number of unsafe tiles?
def increasingNumberOfTilesAndUnsafeTiles():
    question1List = []

    for i in range(2, 12):
        # unsafe tiles is i-1 because otherwise there will be no safe tile to land on
        question1List.append(averageSuccessRate(simulationTimes, 20, 18, i, i-1))

    # This output should be entered into a graph
    print("number of total panes and unsafe tiles increasing from 2 to 12")
    for i in range(len(question1List)):
        print("x:", i + 18, "y:", question1List[i])


# Question 4: increasing number of players
def increasingNumberOfPlayers():
    question1List = []

    for i in range(1, 19):
        # unsafe tiles is i-1 because otherwise there will be no safe tile to land on
        question1List.append(averageSuccessRate(simulationTimes, i, 18, 2, 1))

    # This output should be entered into a graph
    print("Decreasing number of players for baseline bridge")
    for i in range(len(question1List)):
        print("x:", i + 1, "y:", question1List[i])


# Question 5: increasing number of players and segments
def increasingNumberOfPlayersAndSegments():
    question1List = []

    for i in range(0, 10):
        # both start at their baseline value, but increase by 10
        question1List.append(averageSuccessRate(simulationTimes, i+20, i+18, 2, 1))

    # This output should be entered into a graph
    print("Decreasing number of players for baseline bridge")
    for i in range(len(question1List)):
        print("x:", i + 20, "y:", question1List[i])


# Question 6: Calculating the chances of the first player winning
def probabilityOfWinning():
    # Prints a list of odds for the probability of the current player winning
    for i in range(1, 19):
        print(str(i) + ":", oddsOfTheCurrentPlayerSurviving(18, 2, 1, 1, 18-i, 2))


# simulationTimes to specify the number of times all the simulations should run

simulationTimes = 100000

# Comment out functions that should not run

# increasingNumberOfSegments()
# increasingNumberOfTiles()
# increasingNumberOfTilesAndUnsafeTiles()
# increasingNumberOfPlayers()
# increasingNumberOfPlayersAndSegments()
# probabilityOfWinning()
