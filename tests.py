#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

# This file is used for testing functions to insure they return the correct values.

# Imported functions from Python files.
import formulas


# Test function for chooseFormula:

def test_chooseFormula(n, r, expectedOutput):

    result = formulas.chooseFormula(n, r)

    if result == expectedOutput:
        return "Pass: " + str(result)
    else:
        return "Fail: " + str(result)


# This should pass
print(test_chooseFormula(2, 1, 2))
# This should fail
print(test_chooseFormula(0, 1, 2))
# This should pass
print(test_chooseFormula(12345, 3, 313484798540))
