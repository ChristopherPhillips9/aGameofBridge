#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

import math
from math import factorial


# This is where general formulas will be created for use in other parts of the code

def chooseFormula(n, r):
    # This function is the generalized choose formula as shown in the zyBook section 3.3

    # n = the number to be chosen
    # r = the amount to choose

    if n <= 0:
        return "Error, cannot choose from a number <= 0"
    elif n < r:
        return "Error, n cannot be smaller than r"
    else:
        choose = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
        return choose


def oddsOfCurrentPlayerWinning(k, s, p, k1, s1, p1):
    # The goal of this function is to determine the odds of the current players who's playing to win

    # k = panes total
    # s = segments total
    # p = players total
    # k1 = panes remaining in the segment
    # s1 = segments remaining
    # p1 = players remaining

    return 0
