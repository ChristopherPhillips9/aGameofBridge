#!/usr/bin/env python
__author__ = "Christopher Phillips, christopher.phillips9@snhu.edu"

import tkinter as tk

# This generates a GUI
# TODO: better description


def settingsRender(root):
    # Generates the settings menu that holds all the buttons, sliders, etc.
    # Labelframe for keeping things within a framed box
    settingsLabelFrame = tk.LabelFrame(root, text="Settings Menu")
    # settingsLabelFrame.grid(column=0, row=0)
    # settingsLabelFrame.pack(padx=5, pady=5, fill="both", expand=1)

    # Just some test things using the grid.
    label1 = tk.Label(settingsLabelFrame, text="Players")
    label2 = tk.Label(settingsLabelFrame, text="Segments")
    label3 = tk.Label(settingsLabelFrame, text="Panes")

    label1.grid(column=0, row=0)
    label2.grid(column=0, row=1)
    label3.grid(column=0, row=3)

    return settingsLabelFrame


def gameRender(root):
    # Generates the game space that will display the bridge
    # Labelframe for keeping things within a framed box
    gameLabelFrame = tk.LabelFrame(root, text="Game Window")
    # gameLabelFrame.grid(column=0, row=0)
    # gameLabelFrame.pack(padx=5, pady=5, fill="both", expand=1)

    # Just some test things using the grid.
    label1 = tk.Label(gameLabelFrame, text="Outcome")
    label2 = tk.Label(gameLabelFrame, text="Probability")
    label3 = tk.Label(gameLabelFrame, text="Other stuff")

    label1.grid(column=0, row=0)
    label2.grid(column=0, row=1)
    label3.grid(column=0, row=2)

    return gameLabelFrame


def initializeTkinter():
    # Generates the grid that will hold the settings menu and the game window
    # initialize tkinter
    root = tk.Tk()

    # set window title
    root.wm_title("Christopher Phillips - A Game of Bridge")

    # set window size and disable rescaling
    root.geometry("375x400")
    root.resizable("false", "false")

    # Configure frames to display both settings and game
    rootFrame = tk.Frame(root)
    rootFrame.pack(fill="both")

    # Calls the window that displays all the settings. passes root to draw it to the root tk window
    settingsFrame = settingsRender(rootFrame)
    settingsFrame.pack(fill="both", padx=5)

    # Calls the window that displays the playing area and game output
    gameFrame = gameRender(rootFrame)
    gameFrame.pack(fill="both", padx=5)

    # Loop that keeps the window open
    root.mainloop()


# TODO: Remove this after testing
initializeTkinter()
