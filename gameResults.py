#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from gameSimulator import simulateGame


# This function will return the average number of players that reach the end by simulating a specified amount of times
def averageSuccessRate(simulations, players, segments, tiles, unsafe):
    # the array that stores the number of games
    gameResults = []
    # the sum of gameResults
    newGameResults = 0

    # save the results of all the games
    for i in range(simulations):
        gameResults.append(simulateGame(players, segments, tiles, unsafe))

    # calculate the sum of everything in the array
    for i in range(simulations):
        newGameResults = newGameResults + gameResults[i]

    # return the average
    return round((newGameResults / simulations), 2)
