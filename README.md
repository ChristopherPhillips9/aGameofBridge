
# Overview:

This program was created for the final project for MAT-239 at Southern New Hampshire University.
This program simulates the outcome of the bridge game from "Squid Game" with varying parameters.
This document provides a solution for how many people should make it across a given bridge.

## What is a bridge?:
In the popular TV show "Squid Game" the contestants must cross a glass bridge made of multiple segments.
The player must choose between 2 glass pane.
One can support the weight of the player while the other pane will cause the player to fall through.

For this program, a bridge is a nested list containing a randomized assortment of 1's and 0's.
The program will run through each nested list and will perform various actions depending on the values it selects.

An example bridge with 5 segments that have 2 panes and 1 is unsafe pane might look like:

- [[1, 0], [0, 1], [0, 1], [1,0], [0,1]]

### Game vs Simulation:
The program can achieve two goals and both will be mentioned throughout this document.
The game refers to the ability for the user to choose which tiles are selected and play through a given bridge. At the end the user is presented with text that says "you win!" or "you lose!" along with various statistics about the game.

The simulation refers to using a function to guess for a bridge or list of bridges.
This is used to find meaningful data by generating an average number of players surviving a given bridge segment.

### Using the code as a function:
This code has the ability to have several of the functions used for generating meaningful data.
Towards the bottom of this README, the code will be used as a function to generate meaningful data.

## Command Line Interface Documentation:

### main.py overview:
main.py is the CLI of the application. There are 3 functions within main.py.

- programLoop()
- menuSelectionChecker()
- simulationOutput()

programLoop() prints the menu options and waits for an input. If the input is "1" or "2", it will allow the user to enter in game or simulation parameters.
If the user enters "5" to "8" it will run the game or simulation with parameters from the final project.
If a player enters a 9 the program will exit with code 0. This loop will not exit until option 9 is selected.

menuSelectionChecker() is used to determine that the input from the user is valid and wont cause any issues. It is not a complete foolproof system, but ensures some quality of life for using the program.

simulationOutput() provides a human-readable output of simulations from gameResults.averageSuccessRate().

### bridgeRenderer.py overview:
This function is the CLI graphical output for the game board. It contains 3 functions to create a comprehensive experience.

- bridgeObfuscator()
- bridgeGUI()
- endGameScreen

bridgeObfuscator() creates a duplicate of the bridge that has all the 1's and 0's hidden.
It returns the input value of the user's next move
This is the bridge that the user sees.
This duplicated bridge will have its elements replaced with "C" and "X" as the game progresses.
More information about how this bridge is manipulated will be available in gamePlayer overview.</p>

bridgeGUI() displays the game board for the user to use. It contains useful information including:

- Key: █ = unknown tile, X = incorrect guess, C = correct guess.
- Players remaining.
- Chances of the current player surviving.
- The calculated average survival rate for the specified bridge.
- The game board.

endGameScreen() outputs a win or lose screen with game statistics. It contains useful information including:

- A message stating if the player won or lost.
- The specified game parameters.
- The calculated average survival rate for the specified bridge.
- The survivors for this game.

## Function Documentation:

### bridgeGenerator.py overview:
This is the "core" of the program. It generates a random bridge as a nested list (2-D array).

An example bridge with 3 segments, 2 panes, and 1 unsafe pane looks like this:

- [[0, 1], [1, 0], [1, 0]]

The parameters for the bridge are s, k, and c.

- s = The total length of the bridge in segments.
- k = The number of panes.
- c = The number of unsafe panes.

The function begins by creating an empty list called bridgeRow. A for loop runs for the length of the number of segments.
Inside that loop is another for loop that runs for the length of the number of panes.
This loop creates a list called bridgeColumn of all 0's for the length of the number of panes.
This loop has a while loop inside that will run until the number of unsafe panes is reached.
The while loop generates a random number from 0 to the number of unsafe panes.
If the random number corresponds to a 0 in bridgeColumn, it will be replaced with a 1.

Once the bridgeColumn has the correct number of unsafe panes, it will append itself to bridgeRow.
Once bridgeRow reaches the correct number of segments, the function will return the randomized bridge.</p>

### gamePlayer.py overview:

### gameResults.py overview

### gameSimulator.py overview

### pawnGuess.py overview