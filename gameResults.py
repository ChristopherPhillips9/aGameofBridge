#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from gamePlayer import playGame


# This function will return the average number of players that reach the end by simulating a specified amount of times
def averageSuccessRate(times, players, segments, tiles, safe):
    # the array that stores the number of games
    gameResults = []
    # the sum of gameResults
    newGameResults = 0

    # save the results of all the games
    for i in range(times):
        gameResults.append(playGame(players, segments, tiles, safe))

    # calculate the sum of everything in the array
    for i in range(times):
        newGameResults = newGameResults + gameResults[i]

    # return the average
    return round(newGameResults / times)
