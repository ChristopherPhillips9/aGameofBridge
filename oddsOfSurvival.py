#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

# Calculates the odds of the player surviving accounting for already guessed tiles for a given segment


def oddsOfTheCurrentPlayerSurviving(totalSegments, currentPanes, unsafe, currentUnsafe, currentSegment, totalPanes):
    # Calculates the odds of the current player surviving the current segment.
    odds = [((currentPanes - currentUnsafe) / currentPanes)]

    # Calculates the rest of the chances of surviving the panes and adds them up.
    for i in range(totalSegments - currentSegment - 1):
        odds.append((totalPanes - unsafe) / totalPanes)
    print(odds)

    # Multiplies all the odds together
    newOdds = 1

    for i in range(len(odds)):
        newOdds = newOdds * odds[i]

    # Multiplies newOdds by 100 to return a percentage
    newOdds = (newOdds * 100)

    return newOdds

