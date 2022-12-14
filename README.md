
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

These functions allow the game to be played by the user. It contains two functions.

- guessChecker()
- playGame()

guessChecker() is a simple checker to make sure the player enters a value that is correct.
It is not comprehensive of all incorrect inputs.
However, it makes sure that the user does not accidentally input a number out of the range of the segment, or an input of "".
If the user does enter an incorrect input, they are prompted to enter a new number.
The program returns the int of a valid guess.

playGame() takes the input from main.programLoop().
It takes the input of players, segments, tiles, and unsafe tiles.
It creates a copy of the value of players. Next it generates a bridge from bridgeGenerator using the parameters.
Next it creates an obfuscated copy of the bridge from bridgeRenderer.bridgeObfuscator().
Next it specifies that the current segment starts at 0 so that the game starts at the first segment.

A while loop runs through the game until the current segment value reaches the last segment in the bridge.
Inside this loop, the obfuscated bridge, players, and average survival rate for this bridge are all sent to bridgeRenderer.bridgeGUI.
After the user makes a guess, the guess is checked for errors using guessChecker.

The loop checks to see if the guess was correct or not. If the user guessed an element in the list marked 1, the number of players will be decreased.
The element in the obfuscated bridge will also be marked X.
If the number of players reaches 0 then it will run bridgeRenderer.endGameScreen with the "you lose" message.
If the user guessed an element in the list marked 0, the current segment count is advanced by 1.
The element in the obfuscated bridge will also be marked C.
Once the current segment value is equal to the length of the bridge, bridgeRender.endGameScreen will be run with the "you win" message.

### gameResults.py overview

This file contains one function named averageSuccessRate.
It returns the average number of survivors that reach the end of the bridge.

averageSuccessRate() takes the input of simulations, players, segments, tiles, and unsafe tiles.
It creates an array called gameResults that will store all the simulated game outputs.
It also defines an integer to be the sum of the game results.
A for loop will play through all the simulations using the parameters and append them to gameResults.
The function will then add all the results together.
It will return the average number of results rounded to two decimal places

### gameSimulator.py overview

This file contains functions that simulate the game one time. It contains two functions.

- playingBoard()
- simulateGame()

playingBoard() simulates playing through a bridge. It will return the number of players that survive the bridge.
It first defines the remaining players as the number of players specified.
A while loop runs until currentSegment is equal to the length of the bridge.
Unlike the gamePlayer, which makes two separate bridges (one for display, and one as the original bridge),
this program will modify the original bridge. It does so to process which tiles have been guessed and which have not.
Since the bridge will never be seen, there is no reason not to.

First, it gets a guess from pawnGuess.
Next, If the guessed pane is equal to 1, it will subtract 1 from the remaining players. It will also replace the pane value with "X".
If the remaining players are equal to 0, the game will end and the function will return 0.
If the guessed pane is equal to 0, the current segment is advanced. It will also replace the pane value with "C".
If that was the last segment, then the game will return the number of players.

simulateGame() Generates a random bridge and then plays through the game. It saves the results and returns them.

### pawnGuess.py overview

pawnGuess makes a random guess given a segment from a bridge. It contains two functions:

- pawnGuess()
- guessReconstructor()

pawnGuess() creates two empty strings called currentWithoutInt and currentWithoutStr.
It is given the current segment called current.

currentWithoutInt is populated with all 0's for the length of the function.
It then has its 0's replaced with X's that are in the list 'current'.
For example:

- if current = [1, 0, X, 0, X, 1, 0], then currentWithoutInt will equal [0, 0, X, 0, X, 0, 0]

currentWithoutStr has all the int values from current applied to it.
For example:

- if current = [1, 0, X, 0, X, 1, 0] then currentWithoutStr will equal [1, 0, 0, 1, 0]

It will then make a random selection called randomListSelection from currentWithoutInt.
With that value, it will replace the original value in currentWithoutInt. 
It will then take these two lists and run them through guessReconstructor().
It will then return the value that guessReconstructor gave it.

guessReconstructor() takes the two lists. It runs them through a loop for the length of currentWithoutInt.
Every element that is not "X" in currentWithoutInt will be changed to the value from currentWithoutInt.
Once the value of G is found, it will return that value.