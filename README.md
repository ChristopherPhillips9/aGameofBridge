<h1>Overview:</h1>

<p>
This program was created for the final project for MAT-239 at Southern New Hampshire University.
This program simulates the outcome of the bridge game from "Squid Game" with varying parameters.
This document provides a solution for how many people should make it across a given bridge.
</p>

<h2>What is a bridge?:</h2>
<p>
In the popular TV show "Squid Game" the contestants must cross a glass bridge made of multiple segments.
The player must choose between 2 glass pane. One can support the weight of the player while the other pane will cause the player to fall through.

For this program, a bridge is a nested list containing a randomized assortment of 1's and 0's.
The program will run through each nested list and will perform various actions depending on the values it selects.

An example bridge with 5 segments that have 2 panes and 1 is unsafe pane might look like:
<li>[[1, 0], [0, 1], [0, 1], [1,0], [0,1]]</li>
</p>

<h3>Game vs Simulation:</h3>
The program can achieve two goals and both will be mentioned throughout this document.
The game refers to the ability for the user to choose which tiles are selected and play through a given bridge. At the end the user is presented with text that says "you win!" or "you lose!" along with various statistics about the game.

The simulation refers to using a function to guess for a bridge or list of bridges.
This is used to find meaningful data by generating an average number of players surviving a given bridge segment.

<h3>Using the code as a function:</h3>
This code has the ability to be turned into a function with several of the functions available.

<!-- TODO: Expand this! -->

<h3>main.py overview:</h3>

main.py is the CLI of the application. There are 3 functions within main.py.
<li>programLoop()</li>
<li>menuSelectionChecker()</li>
<li>simulationOutput()</li>

programLoop() prints the menu options and waits for an input. If the input is "1" or "2", it will allow the user to enter in game or simulation parameters.
If the user enters "5" to "8" it will run the game or simulation with those given parameters.
If a player enters a 9 the program will exit with code 0. This loop will not exit until option 9 is selected.

menuSelectionChecker() is used to determine that the input from the user is valid and wont cause any issues. It is not a complete foolproof system, but ensures some quality of life for using the program.

simulationOutput() provides a human-readable output of simulations from gameResults.averageSuccessRate().

<h3>bridgeGenerator.py overview:</h3>

<h3>bridgeRenderer.py overview:</h3>

<h3>gamePlayer.py overview:</h3>

<h3>gameResults.py overview</h3>

<h3>gameSimulator.py overview</h3>

<h3>pawnGuess.py overview</h3>