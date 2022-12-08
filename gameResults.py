#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

from gamePlayer import playGame

# the list with all the games in it
gameResults = []

# the sum of gameResults
newGameResults = 0

# How many times to play the game
timesToPlay = 10000

# save the results of all the games
for i in range(timesToPlay):
    gameResults.append(playGame(20, 18, 2, 1))

# add all the sums together
for i in range(timesToPlay):
    newGameResults = newGameResults + gameResults[i]

averageAmountOfWinners = newGameResults / timesToPlay

print(averageAmountOfWinners)
print(gameResults)